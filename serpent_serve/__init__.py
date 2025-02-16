import json
from typing import Any

from grpc import Channel
from tblib import pickling_support

pickling_support.install()
import pickle

from .serpent_pb2 import ArgsKwargs, MethodCall, Response, Result, Error, SetupResponse, Empty, Attr, AttrValue
from .serpent_pb2_grpc import SerpentServicer, SerpentStub


class SerpentServicer(SerpentServicer):

    def __init__(self, inner: Any):
        self.inner = inner

    @property
    def gettables(self):
        return [attr for attr in dir(self.inner) if not callable(getattr(self, attr))]

    def Setup(self, request, context):
        return SetupResponse(
            attributes=[attr for attr in dir(self.inner) if not callable(getattr(self.inner, attr)) and not attr.startswith("__")],
            methods=[meth for meth in dir(self.inner) if callable(getattr(self.inner, meth)) and not meth.startswith("__")]
        )

    def Call(self, request: MethodCall, context: Any) -> Response:
        try:
            args = json.loads(request.argsKwargs.args)
            kwargs = json.loads(request.argsKwargs.kwargs)
            result = getattr(self.inner, request.method)(*args, **kwargs)
            return Response(result=Result(value=json.dumps(result)))
        except Exception as e:
            return Response(error=Error(data=pickle.dumps(e)))

    def GetAttr(self, request: Attr, context):
        value = getattr(self.inner, request.name)
        value = json.dumps(value)
        return Response(result=Result(value=value))

    def SetAttr(self, request: AttrValue, context):
        setattr(self.inner, request.name, json.loads(request.value))
        return Response()


class SerpentClient(SerpentStub):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        setup: SetupResponse = self.Setup(Empty())
        self.__attributes = setup.attributes
        self.__methods = setup.methods

        for attr in self.__attributes:
            self.__add_property(attr)

        for meth in self.__methods:
            self.__add_method(meth)

    def __add_property(self, name):
        def getter(self):
            resp = self.GetAttr(Attr(name=name))
            value = json.loads(resp.result.value)
            return value

        def setter(self, value):
            self.SetAttr(AttrValue(name=name, value=json.dumps(value)))

        setattr(self.__class__, name, property(getter, setter))

    def __add_method(self, name):
        def method(*args: Any, **kwargs: Any) -> Any:
            args = json.dumps(args)
            kwargs = json.dumps(kwargs)
            method_call_data = MethodCall(
                method=name,
                argsKwargs=ArgsKwargs(args=args, kwargs=kwargs))

            response: Response = self.Call(method_call_data)

            if response.HasField("result"):
                return json.loads(response.result.value)
            raise pickle.loads(response.error.data)
        setattr(self, name, method)
