# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.


class ShopAPI:
    def __init__(self):
        self.books = []
        self.orders = []

    def add_book(self, request):
        return business.add_book(request.get("title"), request.get("price_cents"), request.get("stock"))

    def list_books(self):
        return 200, persistence.all_books()
    
    def place_order(book_id, quantity):
        business.place_order(book_id, quantity)

    def get_order(self, order_id):
        return business.get_order(order_id)

