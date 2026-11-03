# Creates the shop, starting with no books and no orders.
#
# STARTING POINT: the shop still uses the layered code from stage 1
# (business.py, persistence.py, presentation.py).
# In step 3 you will build it from the catalog/ and orders/ domains instead.

import catalog.persistence
import catalog.presentation
import orders.persistence
import orders.presentation


def create_app():
    catalog.persistence.reset()
    orders.persistence.reset()
    return ShopAPI()


class ShopAPI:
    def add_book(self, request):
        return catalog.presentation.add_book(request)

    def list_books(self):
        return catalog.presentation.list_books()

    def place_order(self, request):
        return orders.presentation.place_order(request)

    def get_order(self, order_id):
        return orders.presentation.get_order(order_id)
