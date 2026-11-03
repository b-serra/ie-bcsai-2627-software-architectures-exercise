# PRESENTATION LAYER

import business


class ShopAPI:
    def add_book(self, request):
        title = request.get("title")
        price = request.get("price_cents")
        stock = request.get("stock")
        try:
            book = business.add_book(title, price, stock)
        except business.InvalidData as error:
            return 400, {"error": str(error)}
        return 201, book

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        book_id = request.get("book_id")
        quantity = request.get("quantity")
        try:
            order = business.place_order(book_id, quantity)
        except business.InvalidData as error:
            return 400, {"error": str(error)}
        except business.NotFound as error:
            return 404, {"error": str(error)}
        except business.NotEnoughStock as error:
            return 409, {"error": str(error)}
        return 201, order

    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)
        except business.NotFound as error:
            return 404, {"error": str(error)}
        return 200, order
