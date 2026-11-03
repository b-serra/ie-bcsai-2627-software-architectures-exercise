# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.

import business

class ShopAPI:
    def add_book(self, request):
        title = request.get("title")
        price = request.get("price_cents")
        stock = request.get("stock")
        try:
            book = business.add_book(title, price, stock)
            return 201, book

        except business.InvalidData as e:
            return 400, {"error": str(e)}
    
    def list_books(self):
        try: 
            books = business.list_books()
            return 200, books
        except Exception as e:
            return 500, {"error": str(e)}

    def place_order(self, request):
        book_id = request.get("book_id")
        quantity = request.get("quantity")
        try:
            order = business.place_order(book_id, quantity)
            return 201, order
        except business.InvalidData as e:
            return 400, {"error": str(e)}
        except business.NotFound as e:
            return 404, {"error": str(e)}
        except business.NotEnoughStock as e:
            return 409, {"error": str(e)}

    def get_order(self, order_id):
        try:
            order = business.get_order(order_id)
            return 200, order
        except business.NotFound as e:
            return 404, {"error": str(e)}
        return 404, {"error": "order not found"}
