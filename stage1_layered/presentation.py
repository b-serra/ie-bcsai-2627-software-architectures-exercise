# PRESENTATION LAYER: receives requests and returns (status code, body).
# It only calls business.py and turns the errors it raises into status codes.

import business
from business import InvalidData, NotEnoughStock, NotFound


class ShopAPI:
    def add_book(self, request):
        title = request.get("title")
        price = request.get("price_cents")
        stock = request.get("stock")
        try:
            book = business.add_book(title, price, stock)
        except InvalidData as e:
            return 400, {"error": str(e)}
        print("Added book " + book["title"])
        return 201, book






    def list_books(self):
        return 200, business.list_books()



    def place_order(self, request):
        book_id = request.get("book_id")
        quantity = request.get("quantity")
        try:
            order = business.place_order(book_id, quantity)
        except InvalidData as e:
            return 400, {"error": str(e)}
        except NotFound as e:
            return 404, {"error": str(e)}
        except NotEnoughStock as e:
            return 409, {"error": str(e)}
        return 201, order






    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)
        except NotFound as e:
            return 404, {"error": str(e)}
        return 200, order