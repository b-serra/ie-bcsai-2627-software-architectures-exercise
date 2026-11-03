# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    book_id = len(books) + 1
    book = {"id": book_id, "title": title, "price_cents": price_cents, "stock": stock}
    books[book_id] = book
    return book
    # TODO step 1: create the book dict with the next id, store it in `books` and return it


def find_book(book_id):
    if book_id in books:
        return books[book_id]
    return None
    # TODO step 1: return the book, or None if it does not exist


def all_books():
    return list(books.values())
    # TODO step 1: return a list with all the books


def update_stock(book_id, new_stock):
    if book_id in books:
        books[book_id]["stock"] = new_stock
    # TODO step 1: change the stock of the book


def save_order(order):
    order_id = len(orders) + 1
    order["id"] = order_id
    orders[order_id] = order
    return order
    # TODO step 1: give the order the next id, store it in `orders` and return it

def find_order(order_id):
    if order_id in orders:
        return orders[order_id]
    return None
    # TODO step 1: return the order, or None if it does not exist
