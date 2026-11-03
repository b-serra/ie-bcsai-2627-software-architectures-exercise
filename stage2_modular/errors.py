# Errors shared by all domains, and how presentation turns them into status codes.


class ShopError(Exception):
    def __init__(self, message):
        if not isinstance(self, ShopError):
            raise TypeError("ShopError must be subclassed")
        super().__init__(message)

class InvalidData(ShopError):
    def __init__(self, message):
        if not isinstance(self, InvalidData):
            raise TypeError("InvalidData must be subclassed")
        super().__init__(message)


class NotFound(ShopError):
    def __init__(self, message):
        if not isinstance(self, NotFound):
            raise TypeError("NotFound must be subclassed")
        super().__init__(message)


class NotEnoughStock(ShopError):
    def __init__(self, message):
        if not isinstance(self, NotEnoughStock):
            raise TypeError("NotEnoughStock must be subclassed")
        super().__init__(message)


STATUS_CODES = {InvalidData: 400, NotFound: 404, NotEnoughStock: 409}


def error_response(error):
    return STATUS_CODES[type(error)], {"error": str(error)}
