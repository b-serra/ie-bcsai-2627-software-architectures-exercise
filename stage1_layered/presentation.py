# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.

import business
from business import InvalidData, NotFound, NotEnoughStock


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"),
                request.get("price_cents"),
                request.get("stock"),
            )
            return 201, book
        except InvalidData:
            return 400, {"error": "invalid data"}

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(
                request.get("book_id"),
                request.get("quantity"),
            )
            return 201, order
        except InvalidData:
            return 400, {"error": "invalid data"}
        except NotFound:
            return 404, {"error": "not found"}
        except NotEnoughStock:
            return 409, {"error": "not enough stock"}

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except NotFound:
            return 404, {"error": "order not found"}