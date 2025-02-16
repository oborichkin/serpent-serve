from typing import Any


class CustomError(Exception):
    pass


class GenericClass:

    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def return_same(self, a: Any) -> Any:
        return a

    def raises_exception(self):
        raise Exception("I am default exception")

    def raises_value_error(self):
        raise ValueError("Indeed, a value error")

    def raises_custom_error(self):
        raise CustomError(1, 2, 3, "I am custom error")
