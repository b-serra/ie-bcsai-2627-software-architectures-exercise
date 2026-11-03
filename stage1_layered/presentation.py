# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.

import business
from business import InvalidData, NotFound, NotEnoughStock


def error_response(error):
    if isinstance(error, InvalidData):
        return 400, {"error": str(error)}
    if isinstance(error, NotFound):
        return 404, {"error": str(error)}
    if isinstance(error, NotEnoughStock):
        return 409, {"error": str(error)}
    raise error


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"), request.get("price_cents"), request.get("stock")
            )
        except business.ShopError as error:
            return error_response(error)
        return 201, book

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(request.get("book_id"), request.get("quantity"))
        except business.ShopError as error:
            return error_response(error)
        return 201, order

    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)
        except business.ShopError as error:
            return error_response(error)
        return 200, order