from catalog import persistence as catalog_store
from catalog import presentation as catalog_api
from orders import persistence as orders_store
from orders import presentation as orders_api


class ShopAPI:
    add_book = staticmethod(catalog_api.add_book)
    list_books = staticmethod(catalog_api.list_books)
    place_order = staticmethod(orders_api.place_order)
    get_order = staticmethod(orders_api.get_order)


def create_app():
    catalog_store.reset()
    orders_store.reset()
    return ShopAPI()
