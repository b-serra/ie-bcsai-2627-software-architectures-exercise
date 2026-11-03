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
    # TODO step 2: check the data (raise InvalidData) and save the book with persistence.save_book
    title = title
    price = price_cents
    stock = stock

    if type(title) != str or title == "":
        raise InvalidData("title is required")
    if type(price) != int or price <= 0:
        raise InvalidData("price must be a positive integer")
    if type(stock) != int or stock < 0:
        raise InvalidData("stock cannot be negative")
    return persistence.save_book(title, price, stock)



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
    book_id = book_id
    quantity = quantity
    if type(book_id) != int or type(quantity) != int or quantity < 1:
        raise InvalidData("invalid data type")
    
    book = persistence.find_book(book_id)
    if not book:
        raise NotFound("book does not exist")
    if book["stock"] < quantity:
        raise NotEnoughStock("Not enough stock")
    
    subtotal = book["price_cents"] * quantity
    shipping = calculate_shipping(subtotal)
    
    persistence.update_stock(book_id, book["stock"] - quantity)

    order = persistence.save_order(
        {
        "book_id": book_id,
        "quantity": quantity,
        "subtotal_cents": subtotal,
        "shipping_cents": shipping,
        "total_cents": subtotal + shipping,
        }
    )
    return order


def get_order(order_id):
    # TODO step 2: return the order, or raise NotFound
    order = persistence.find_order(order_id)
    if order is None:
        raise NotFound("order does not exist")
    return order
