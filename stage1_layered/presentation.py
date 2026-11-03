# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.
import business
from business import InvalidData, NotFound, OutOfStock

class ShopAPI:
  

    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"), request.get("price"), request.get("stock")
            )
        except InvalidData as e:
            return 400, {"error": str(e)}
        return 201, book

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(request.get("book_id"), request.get("quantity"))
        except InvalidData as e:
            return 400, {"error": str(e)}
        except NotFound as e:
            return 404, {"error": str(e)}
        except OutOfStock as e:
            return 409, {"error": str(e)}
        return 201, order

    

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except NotFound as e:
            return 404, {"error": str(e)}
