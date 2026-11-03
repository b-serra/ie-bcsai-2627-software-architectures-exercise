# PRESENTATION LAYER: receives requests and returns (status code, body).
# It calls the business layer and turns errors into status codes.

import business
from business import ShopError, InvalidData, NotFound, NotEnoughStock


STATUS_CODES = {InvalidData: 400, NotFound: 404, NotEnoughStock: 409}


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"),
                request.get("price_cents"),
                request.get("stock"),
            )
            return 201, book
        except ShopError as e:
            return STATUS_CODES[type(e)], {"error": str(e)}

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(
                request.get("book_id"),
                request.get("quantity"),
            )
            return 201, order
        except ShopError as e:
            return STATUS_CODES[type(e)], {"error": str(e)}

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except ShopError as e:
            return STATUS_CODES[type(e)], {"error": str(e)}
        