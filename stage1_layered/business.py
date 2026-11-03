# BUSINESS LAYER: the rules of the shop.
# It uses the persistence layer to store and find data.
# It knows nothing about requests or status codes: when something is wrong it raises an error.

import persistence

FREE_SHIPPING_FROM = 5000  # cents
SHIPPING_PRICE = 499  # cents


class ShopError(Exception):
    pass


class InvalidData(ShopError):
    pass


class NotFound(ShopError):
    pass


class NotEnoughStock(ShopError):
    pass


def _valid_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


def _valid_text(value):
    return isinstance(value, str) and value.strip() != ""


def calculate_shipping(subtotal_cents):
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    return SHIPPING_PRICE


def add_book(title, price_cents, stock):
    if not _valid_text(title) or not _valid_int(price_cents) or not _valid_int(stock):
        raise InvalidData()
    if price_cents <= 0 or stock < 0:
        raise InvalidData()
    return persistence.save_book(title, price_cents, stock)

def list_books():
    return persistence.all_books()


def place_order(book_id, quantity):
    if not _valid_int(book_id) or not _valid_int(quantity):
        raise InvalidData()
    if book_id <= 0 or quantity <= 0:
        raise InvalidData()

    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound()

    if book["stock"] < quantity:
        raise NotEnoughStock()

    subtotal_cents = book["price_cents"] * quantity
    shipping_cents = calculate_shipping(subtotal_cents)

    persistence.update_stock(book_id, book["stock"] - quantity)

    order = {
        "book_id": book_id,
        "quantity": quantity,
        "subtotal_cents": subtotal_cents,
        "shipping_cents": shipping_cents,
        "total_cents": subtotal_cents + shipping_cents,
    }
    return persistence.save_order(order)


def get_order(order_id):
    order = persistence.find_order(order_id)
    if order is None:
        raise NotFound()
    return order