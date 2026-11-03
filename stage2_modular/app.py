# Creates the shop from the catalog and orders domains, starting with no books and no orders.

from types import SimpleNamespace

from catalog import persistence as catalog_persistence
from catalog import presentation as catalog
from orders import persistence as orders_persistence
from orders import presentation as orders


def create_app() -> SimpleNamespace:
    catalog_persistence.reset()
    orders_persistence.reset()
    return SimpleNamespace(
        add_book    = catalog.add_book,
        list_books  = catalog.list_books,
        place_order = orders.place_order,
        get_order   = orders.get_order,
    )
