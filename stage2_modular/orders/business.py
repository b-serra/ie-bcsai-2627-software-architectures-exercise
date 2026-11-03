# ORDERS - BUSINESS: the rules about orders and prices.
# Everything about books is asked to the catalog's business layer.
# Orders never touches the catalog's persistence.

from catalog import business as catalog
from errors import InvalidData, NotFound
from orders import persistence

FREE_SHIPPING_FROM = 5000  # cents
SHIPPING_PRICE = 499  # cents


def calculate_shipping(subtotal_cents):
    # TODO step 2: move the code from the old business.py here
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    else:
        return SHIPPING_PRICE


def place_order(book_id, quantity):
    # TODO step 2: move the code from the old business.py here, but everything about the book
    #   goes through the catalog: catalog.get_price() and catalog.take_stock()
    if type(book_id) != int or type(quantity) != int or quantity < 1:
        raise InvalidData

    book = catalog.persistence.find_book(book_id)

    subtotal = catalog.get_price(book_id)

    book["stock"] = catalog.take_stock(book_id, quantity)
    order = {
        "id": len(persistence.orders) + 1,
        "book_id": book_id,
        "quantity": quantity,
        "subtotal_cents": subtotal,
        "shipping_cents": calculate_shipping(subtotal),
        "total_cents": subtotal + calculate_shipping(subtotal),
    }
    persistence.save_order(order)
    return order


def get_order(order_id):
    # TODO step 2: move the code from the old business.py here
    order = persistence.find_order(order_id)
    if order == None:
        raise NotFound
    else:
        return order
    raise NotImplementedError("TODO step 2")
