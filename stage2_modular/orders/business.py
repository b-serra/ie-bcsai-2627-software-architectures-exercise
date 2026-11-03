# ORDERS - BUSINESS: the rules about orders and prices.
# Everything about books is asked to the catalog's business layer.
# Orders never touches the catalog's persistence.

from catalog import business as catalog
from errors import InvalidData, NotFound
from orders import persistence

FREE_SHIPPING_FROM = 5000  # cents
SHIPPING_PRICE = 499  # cents

def _valid_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


def calculate_shipping(subtotal_cents):
    # TODO step 2: move the code from the old business.py here
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    return SHIPPING_PRICE


def place_order(book_id, quantity):
    # TODO step 2: move the code from the old business.py here, but everything about the book
    #   goes through the catalog: catalog.get_price() and catalog.take_stock()
    if not _valid_int(book_id) or not _valid_int(quantity) or quantity < 1:
        raise InvalidData()
    if book_id <= 0 or quantity <= 0:
        raise InvalidData()
    try:
        price_cents = catalog.get_price(book_id)
        catalog.take_stock(book_id, quantity)
    except catalog.NotFound:
        raise NotFound()
    subtotal = price_cents * quantity
    shipping = calculate_shipping(subtotal)
    order = {"book_id": book_id, "quantity": quantity, "subtotal_cents": subtotal, "shipping_cents": shipping, "total_cents": subtotal + shipping}
    return persistence.save_order(order)

def get_order(order_id):
    # TODO step 2: move the code from the old business.py here
    order = persistence.find_order(order_id)
    if not order:
        raise NotFound()
    return order
