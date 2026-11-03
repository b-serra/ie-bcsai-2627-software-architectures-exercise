# PRESENTATION LAYER: receives requests and returns (status code, body).
# It only calls business.py and turns its errors into status codes.
# No shop rules and no stored data here.

import business

STATUS_FOR_ERROR = {
    business.InvalidData: 400,
    business.NotFound: 404,
    business.NotEnoughStock: 409,
}


def error_response(error):
    return STATUS_FOR_ERROR[type(error)], {"error": str(error)}


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
