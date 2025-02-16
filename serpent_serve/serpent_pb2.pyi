from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArgsKwargs(_message.Message):
    __slots__ = ("args", "kwargs")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    KWARGS_FIELD_NUMBER: _ClassVar[int]
    args: str
    kwargs: str
    def __init__(self, args: _Optional[str] = ..., kwargs: _Optional[str] = ...) -> None: ...

class MethodCall(_message.Message):
    __slots__ = ("method", "argsKwargs")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ARGSKWARGS_FIELD_NUMBER: _ClassVar[int]
    method: str
    argsKwargs: ArgsKwargs
    def __init__(self, method: _Optional[str] = ..., argsKwargs: _Optional[_Union[ArgsKwargs, _Mapping]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: Result
    error: Error
    def __init__(self, result: _Optional[_Union[Result, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class SetupResponse(_message.Message):
    __slots__ = ("attributes", "methods")
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedScalarFieldContainer[str]
    methods: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, attributes: _Optional[_Iterable[str]] = ..., methods: _Optional[_Iterable[str]] = ...) -> None: ...

class Attr(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AttrValue(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
