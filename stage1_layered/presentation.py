
# PRESENTATION LAYER: receives requests and returns (status code, body).
# Business rules belong to business.py.
# Data storage belongs to persistence.py.

import business


class ShopAPI:
    def __init__(self):
        # Reset the shop through the business layer.
        business.reset_shop()

    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"),
                request.get("price_cents"),
                request.get("stock")
            )
            print("Added book " + book["title"])
            return 201, book
        except business.InvalidData as error:
            return 400, {"error": str(error)}

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(
                request.get("book_id"),
                request.get("quantity")
            )
            book = business.get_book(order["book_id"])
            print("Order placed for " + book["title"])
            return 201, order
        except business.InvalidData as error:
            return 400, {"error": str(error)}
        except business.NotFound as error:
            return 404, {"error": str(error)}
        except business.NotEnoughStock as error:
            return 409, {"error": str(error)}

    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)
            return 200, order
        except business.NotFound as error:
            return 404, {"error": str(error)}
