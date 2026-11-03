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
    if not title or price_cents <= 0 or stock < 0:
        raise InvalidData("Invalid book data")
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
    if quantity <= 0:
        raise InvalidData("Quantity must be greater than zero")
    book = persistence.find_book(book_id)
    if not book:
        raise NotFound("Book not found")
    if book["stock"] < quantity:
        raise NotEnoughStock("Not enough stock available")
    subtotal = book["price_cents"] * quantity
    shipping = calculate_shipping(subtotal)
    total = subtotal + shipping
    persistence.update_stock(book_id, book["stock"] - quantity)
    order = {"book_id": book_id, "quantity": quantity, "subtotal_cents": subtotal, "shipping_cents": shipping, "total_cents": total}
    return persistence.save_order(order)




def get_order(order_id):
    # TODO step 2: return the order, or raise NotFound
    order = persistence.find_order(order_id)
    if not order:
        raise NotFound("Order not found")
    return order

