from typing import Any


class NotNumericError(Exception):
    """This is used when type casting or setting a variable"""

    def __init__(
        self,
        value: Any,
        message: str = "The value was not of numeric type but numeric type was required",
    ):
        self.value = value
        self.message = message
        super().__init__(self)

    def __str__(self):
        return f"`{self.value}` -> {self.message}"


class ValueIsNoneError(Exception):
    def __init__(
        self,
        value: None,
        message: str = "The value given was unexpectedly None",
    ):
        self.value = value
        self.message = message
        super().__init__(self)

    def __str__(self):
        return f"`{self.value}` -> {self.message}"
