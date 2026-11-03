# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.



import business

class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"),
                request.get("price_cents"),
                request.get("stock")
            )
            return 201, book
        except business.InvalidData as e:
            return 400, {"error": str(e)}

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(
                request.get("book_id"),
                request.get("quantity")
            )
            return 201, order
        except business.InvalidData as e:
            return 400, {"error": str(e)}
        except business.NotFound as e:
            return 404, {"error": str(e)}
        except business.NotEnoughStock as e:
            return 409, {"error": str(e)}

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except business.NotFound as e:
            return 404, {"error": str(e)}
