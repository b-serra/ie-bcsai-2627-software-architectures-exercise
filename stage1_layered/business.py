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
    return SHIPPING_PRICE


def add_book(title, price_cents, stock):
    # TODO step 2: check the data (raise InvalidData) and save the book with persistence.save_book
    if not title or price_cents < 0 or stock < 0:
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
       def place_order(self, request):
        book_id = request.get("book_id")
        quantity = request.get("quantity")
        if type(book_id) != int or type(quantity) != int or quantity < 1:
            raise InvalidData("Invalid book_id or quantity")

        book = None
        for b in self.books:
            if b["id"] == book_id:
                book = b
        if book == None:
            raise NotFound("Book not found")
        if book["stock"] < quantity:
            raise NotEnoughStock("Not enough stock")

        subtotal = book["price_cents"] * quantity
        if subtotal >= 5000:
            shipping = 0
        else:
            shipping = 499

        book["stock"] = book["stock"] - quantity
        order = {
            "id": len(self.orders) + 1,
            "book_id": book_id,
            "quantity": quantity,
            "subtotal_cents": subtotal,
            "shipping_cents": shipping,
            "total_cents": subtotal + shipping,
        }
        self.orders.append(order)
        print("Order placed for " + book["title"])
        persistence.update_stock(book_id, book["stock"])
        persistence.save_order(order)
        return 201, order

def get_order(self, order_id):
    for o in self.orders:
        if o["id"] == order_id:
            return 200, o
    raise NotFound("Order not found")
