# Creates the shop, starting with no books and no orders.
# The shop is built from the two domains: catalog/ and orders/.

from catalog import persistence as catalog_persistence
from catalog import presentation as catalog
from orders import persistence as orders_persistence
from orders import presentation as orders


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
    catalog_persistence.reset()
    orders_persistence.reset()
    return ShopAPI()
