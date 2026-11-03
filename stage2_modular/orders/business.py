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
    return SHIPPING_PRICE


def place_order(book_id, quantity):
    # TODO step 2: move the code from the old business.py here, but everything about the book
    #   goes through the catalog: catalog.get_price() and catalog.take_stock()
    if type(book_id) != int or type(quantity) != int or quantity < 1:
        raise InvalidData("book_id and a positive quantity are required")
    price = catalog.get_price(book_id)
    subtotal = price * quantity
    shipping = calculate_shipping(subtotal)
    catalog.take_stock(book_id, quantity)
    return persistence.save_order(
        {
            "book_id": book_id,
            "quantity": quantity,
            "subtotal_cents": subtotal,
            "shipping_cents": shipping,
            "total_cents": subtotal + shipping,
        }
    )


def get_order(order_id):
    # TODO step 2: move the code from the old business.py here
    order = persistence.find_order(order_id)
    if order is None:
        raise NotFound("order not found")
    return order
