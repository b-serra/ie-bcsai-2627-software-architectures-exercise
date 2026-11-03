# PRESENTATION LAYER: receives requests and returns (status code, body).
# It only calls the business layer and turns its errors into status codes.

import business
from business import InvalidData, NotEnoughStock, NotFound, ShopError

STATUS_CODES = {InvalidData: 400, NotFound: 404, NotEnoughStock: 409}


def error_response(error):
    return STATUS_CODES[type(error)], {"error": str(error)}


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(request.get("title"), request.get("price_cents"), request.get("stock"))
            return 201, book
        except ShopError as error:
            return error_response(error)

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(request.get("book_id"), request.get("quantity"))
            return 201, order
        except ShopError as error:
            return error_response(error)

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except ShopError as error:
            return error_response(error)