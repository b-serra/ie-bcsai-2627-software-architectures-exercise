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
    # TODO step 2: 0 from FREE_SHIPPING_FROM cents, otherwise SHIPPING_PRICE
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    else:
        return SHIPPING_PRICE


def add_book(title, price_cents, stock):
    # TODO step 2: check the data (raise InvalidData) and save the book with persistence.save_book
    if type(title) != str or title == "":
        raise InvalidData()
    if type(price_cents) != int or price_cents <= 0:
        raise InvalidData()
    if type(stock) != int or stock < 0:
        raise InvalidData()
    return persistence.save_book(title, price_cents, stock)


def list_books():
    # TODO step 2: return all the books, using the persistence layer
    return persistence.all_books()


def place_order(book_id, quantity):
    # TODO step 2: move the order logic from presentation.py here.
    #   invalid book_id or quantity -> raise InvalidData
    #   book does not exist         -> raise NotFound
    #   not enough stock            -> raise NotEnoughStock
    #   otherwise: compute the price (use calculate_shipping), update the stock,
    #   save the order and return it (use the persistence layer)
    if type(book_id) != int or type(quantity) != int or quantity <= 0:
        raise InvalidData()
    if book_id not in persistence.books:
        raise NotFound()
    book = persistence.books[book_id]
    if quantity > book["stock"]:
        raise NotEnoughStock()

    subtotal = book["price_cents"] * quantity
    shipping = calculate_shipping(subtotal)
    persistence.update_stock(book_id, book["stock"] - quantity)

    order = {
        "book_id": book_id,
        "quantity": quantity,
        "subtotal_cents": subtotal,
        "shipping_cents": shipping,
        "total_cents": subtotal + shipping,
    }
    return persistence.save_order(order)
     

def get_order(order_id):
    # TODO step 2: return the order, or raise NotFound
    if order_id in persistence.orders:
        return persistence.orders[order_id]
    else:
        raise NotFound()
