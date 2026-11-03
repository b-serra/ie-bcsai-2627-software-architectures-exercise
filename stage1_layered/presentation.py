# PRESENTATION LAYER: receives requests and returns (status code, body).
# It only calls the business layer and turns its errors into status codes.
# It does not store data and contains no shop rules.

import business
from business import InvalidData, NotEnoughStock, NotFound


def error_response(error):
    if isinstance(error, InvalidData):
        status = 400
    elif isinstance(error, NotFound):
        status = 404
    elif isinstance(error, NotEnoughStock):
        status = 409
    else:
        status = 500
    return status, {"error": str(error)}


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(request.get("title"), request.get("price_cents"), request.get("stock"))
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
