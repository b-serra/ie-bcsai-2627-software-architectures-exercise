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


def calculate_shipping(subtotal_cents):
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    return SHIPPING_PRICE


def add_book(title, price_cents, stock):
    if type(title) != str or title == "":
        raise InvalidData("title is required")
    if type(price_cents) != int or price_cents <= 0:
        raise InvalidData("price must be a positive integer")
    if type(stock) != int or stock < 0:
        raise InvalidData("stock can't be negative")
    return persistence.save_book(title, price_cents, stock)


def list_books():
    return persistence.all_books()


def place_order(book_id, quantity):
    # TODO step 2: move the order logic from presentation.py here.
    #   invalid book_id or quantity -> raise InvalidData
    #   book does not exist         -> raise NotFound
    #   not enough stock            -> raise NotEnoughStock
    #   otherwise: compute the price (use calculate_shipping), update the stock,
    #   save the order and return it (use the persistence layer)
    if type(book_id) != int or type(quantity) != int or quantity < 1:
        raise InvalidData("Invalid book_id or quantity")
    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound("Book not found")
    if book["stock"] < quantity:
        raise NotEnoughStock("Not enough stock")
    subtotal = book["price_cents"] * quantity
    shipping = calculate_shipping(subtotal)
    total = subtotal + shipping
    persistence.update_stock(book_id, book["stock"] - quantity)
    order = {
        "book_id": book_id,
        "quantity": quantity,
        "subtotal_cents": subtotal,
        "shipping_cents": shipping,
        "total_cents": total,
    }
    return persistence.save_order(order)
    


def get_order(order_id):
    order = persistence.find_order(order_id)
    if order is None:
        raise NotFound("Order not found")
    return order
