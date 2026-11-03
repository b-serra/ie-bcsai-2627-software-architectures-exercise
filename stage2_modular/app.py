# Creates the shop, starting with no books and no orders.
# The shop is built from the two domains: catalog and orders.

from types import SimpleNamespace

from catalog import persistence as catalog_storage
from catalog import presentation as catalog_api
from orders import persistence as orders_storage
from orders import presentation as orders_api


def create_app():
    catalog_storage.reset()
    orders_storage.reset()
    return SimpleNamespace(
        add_book = catalog_api.add_book,
        list_books = catalog_api.list_books,
        place_order = orders_api.place_order,
        get_order = orders_api.get_order
    )