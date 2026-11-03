# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    id = len(books) + 1
    books[id] = {'id': id, "title": title, "price_cents": price_cents, "stock": stock}
    # TODO step 1: create the book dict with the next id, store it in `books` and return it
    return books[id]


def find_book(book_id):
    return books.get(book_id)
    # TODO step 1: return the book, or None if it does not exist


def all_books():
    # TODO step 1: return a list with all the books
    return books.values()


def update_stock(book_id, new_stock):
    if not books[book_id]:
        return None
    books[book_id]['stock'] = new_stock
    return books[book_id]
    # TODO step 1: change the stock of the book


def save_order(order):
    id = len(orders) + 1
    order['id'] = id
    orders[id] = order
    return orders[id]
    # TODO step 1: give the order the next id, store it in `orders` and return it


def find_order(order_id):
    return orders.get(order_id)
    # TODO step 1: return the order, or None if it does not exist
