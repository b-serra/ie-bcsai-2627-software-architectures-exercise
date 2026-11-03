# PRESENTATION LAYER: receives requests and returns (status code, body).
# Shop rules and storage live in the business and persistence layers.

import business


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"), request.get("price_cents"), request.get("stock")
            )
        except business.InvalidData:
            return 400, {"error": "invalid book data"}
        return 201, book

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(request.get("book_id"), request.get("quantity"))
        except business.InvalidData:
            return 400, {"error": "book_id and a positive quantity are required"}
        except business.NotFound:
            return 404, {"error": "book not found"}
        except business.NotEnoughStock:
            return 409, {"error": "not enough stock"}
        return 201, order

    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)
        except business.NotFound:
            return 404, {"error": "order not found"}
        return 200, order
