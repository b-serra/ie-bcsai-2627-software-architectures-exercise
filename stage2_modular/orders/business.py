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
    if not isinstance(subtotal_cents, int):
        raise InvalidData("subtotal_cents must be an int")
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    return SHIPPING_PRICE


def place_order(book_id, quantity):
    # TODO step 2: move the code from the old business.py here, but everything about the book
    #   goes through the catalog: catalog.get_price() and catalog.take_stock()
    if not isinstance(book_id, int):
        raise InvalidData("book_id must be an int")
    if not isinstance(quantity, int):
        raise InvalidData("quantity must be an int")
    book = catalog.get_book(book_id)
    if book is None:
        raise NotFound(f"book {book_id} not found")
    price_cents = book["price_cents"]
    subtotal_cents = price_cents * quantity
    shipping_cents = calculate_shipping(subtotal_cents)
    total_cents = subtotal_cents + shipping_cents
    catalog.take_stock(book_id, quantity)
    order = persistence.create_order(book_id, quantity, subtotal_cents, shipping_cents, total_cents)
    return order


def get_order(order_id):
    # TODO step 2: move the code from the old business.py here
    if not isinstance(order_id, int):
        raise InvalidData("order_id must be an int")
    order = persistence.get_order(order_id)
    if order is None:
        raise NotFound(f"order {order_id} not found")
    return order
