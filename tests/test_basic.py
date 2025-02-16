import pytest
from .models import GenericClass, CustomError


def test_method_call(client: GenericClass):
    assert client.return_same(1) == 1
    assert client.return_same('foo') == 'foo'
    assert client.return_same(None) is None
    assert client.return_same([]) == []
    assert client.return_same([1,2,3]) == [1,2,3]
    assert client.return_same({}) == {}
    assert client.return_same({"a": 1, "b": None, "c": "str"}) == {"a": 1, "b": None, "c": "str"}
    assert client.return_same((1,2,3)) == [1,2,3]


def test_attr_getter(client: GenericClass, instance: GenericClass):
    assert instance.a == client.a
    assert instance._b == client._b
    assert instance._GenericClass__c == client._GenericClass__c


def test_attr_setter(client: GenericClass, instance: GenericClass):
    assert instance.a == client.a
    client.a = 111
    assert instance.a == client.a
    instance.a = 222
    assert instance.a == client.a


@pytest.mark.parametrize("exception,method", [
    (Exception, "raises_exception"),
    (ValueError, "raises_value_error"),
    (Exception, "raises_custom_error"),
    (CustomError, "raises_custom_error"),
])
def test_raise_exception(client: GenericClass, exception, method):
    with pytest.raises(exception):
        getattr(client, method)()
