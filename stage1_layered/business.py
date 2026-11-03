# BUSINESS LAYER: the rules of the shop.
# It uses the persistence layer to store and find data.
# It knows nothing about requests or status codes: when something is wrong it raises an error.

import persistence

FREE_SHIPPING_FROM = 5000  # cents
SHIPPING_PRICE = 499  # cents

class ShopError(Exception):
    def __init__(self, message):
        if not isinstance(self, ShopError):
            raise TypeError("ShopError must be subclassed")
        super().__init__(message)

class InvalidData(ShopError):
    def __init__(self, message):
        if not isinstance(self, InvalidData):
            raise TypeError("InvalidData must be subclassed")
        super().__init__(message)

class NotFound(ShopError):
    def _init__(self, message):
        if not isinstance(self, NotFound):
            raise TypeError("NotFound must be subclassed")
        super().__init__(message)

class NotEnoughStock(ShopError):
    def __init__(self, message):
        if not isinstance(self, NotEnoughStock):
            raise TypeError("NotEnoughStock must be subclassed")
        super().__init__(message)

def calculate_shipping(subtotal_cents):
    # TODO step 2: 0 from FREE_SHIPPING_FROM cents, otherwise SHIPPING_PRICE
    if subtotal_cents >= FREE_SHIPPING_FROM:
        return 0
    else:
        return SHIPPING_PRICE

def add_book(title, price_cents, stock):
    # TODO step 2: check the data (raise InvalidData) and save the book with persistence.save_book
    if not title:
        raise InvalidData("Book title is required")
    if price_cents <= 0:
        raise InvalidData("Book price must be a positive number")
    if stock < 0:
        raise InvalidData("Book stock cannot be negative")
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
    if not isinstance(book_id, int) or not isinstance(quantity, int) or quantity < 1:
        raise InvalidData("book_id and a positive quantity are required")
    book = persistence.find_book(book_id)
    if not book:
        raise NotFound("Book not found")
    if book['stock'] < quantity:
        raise NotEnoughStock("Not enough stock available")
    subtotal_cents = book['price_cents'] * quantity
    shipping_cents = calculate_shipping(subtotal_cents)
    total_cents = subtotal_cents + shipping_cents
    persistence.update_stock(book_id, book['stock'] - quantity)
    order = {
        'book_id': book_id,
        'quantity': quantity,
        'subtotal_cents': subtotal_cents,
        'shipping_cents': shipping_cents,
        'total_cents': total_cents
    }
    return persistence.save_order(order)

def get_order(order_id):
    # TODO step 2: return the order, or raise NotFound
    order = persistence.find_order(order_id)
    if not order:
        raise NotFound("Order not found")
    return order
