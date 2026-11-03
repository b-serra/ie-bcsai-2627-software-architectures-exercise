# Creates the shop, starting with no books and no orders.
#
# STARTING POINT: the shop still uses the layered code from stage 1
# (business.py, persistence.py, presentation.py).
# In step 3 you will build it from the catalog/ and orders/ domains instead.


from catalog import presentation as catalog
from orders import presentation as orders
from catalog import persistence as catalog_db
from orders import persistence as orders_db

class ShopAPI:
    def add_book(self, request):
        return catalog.add_book(request)

    def list_books(self):
        return catalog.list_books()

    def place_order(self, request):
        return orders.place_order(request)

    def get_order(self, order_id):
        return orders.get_order(order_id)


def create_app():
    catalog_db.reset()
    orders_db.reset()
    return ShopAPI()
