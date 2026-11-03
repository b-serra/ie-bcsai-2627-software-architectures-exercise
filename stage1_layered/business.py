# BUSINESS LAYER: the rules of the shop.
# It uses the persistence layer to store and find data.
# It knows nothing about requests or status codes: when something is wrong it raises an error.

import persistence

FREE_SHIPPING_FROM = 5000
SHIPPING_PRICE     = 499


class ShopError(Exception):
    pass


class InvalidData(ShopError):
    pass


class NotFound(ShopError):
    pass


class NotEnoughStock(ShopError):
    pass


def calculate_shipping(subtotal_cents: int) -> int:
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    return SHIPPING_PRICE


def add_book(title: str, price_cents: int, stock: int) -> dict:
    if type(title) is not str or title == '':
        raise InvalidData('title is required')
    if type(price_cents) is not int or price_cents <= 0:
        raise InvalidData('price must be a positive integer')
    if type(stock) is not int or stock < 0:
        raise InvalidData('stock cannot be negative')

    return persistence.save_book(title, price_cents, stock)


def list_books() -> list[dict]:
    return persistence.all_books()


def place_order(book_id: int, quantity: int) -> dict:
    if type(book_id) is not int or type(quantity) is not int or quantity < 1:
        raise InvalidData('book_id and a positive quantity are required')

    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound('book not found')
    if book['stock'] < quantity:
        raise NotEnoughStock('not enough stock')

    subtotal = book['price_cents'] * quantity
    shipping = calculate_shipping(subtotal)

    persistence.update_stock(book_id, book['stock'] - quantity)
    return persistence.save_order({
        'book_id'       : book_id,
        'quantity'      : quantity,
        'subtotal_cents': subtotal,
        'shipping_cents': shipping,
        'total_cents'   : subtotal + shipping,
    })


def get_order(order_id: int) -> dict:
    order = persistence.find_order(order_id)
    if order is None:
        raise NotFound('order not found')
    return order
