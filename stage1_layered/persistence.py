# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    book_id = len(books) + 1
    book = {
        "id": book_id,
        "title": title,
        "price_cents": price_cents,
        "stock": stock,
    }
    books[book_id] = book
    return book


def find_book(book_id):
    # TODO step 1: return the book, or None if it does not exist
    return books.get(book_id)


def all_books():
    # TODO step 1: return a list with all the books
    return list(books.values())


def update_stock(book_id, new_stock):
    # TODO step 1: change the stock of the book
    book = find_book(book_id)
    if book:
        book["stock"] = new_stock


def save_order(order):
    # TODO step 1: give the order the next id, store it in `orders` and return it
    order_id = len(orders) + 1
    order["id"] = order_id
    orders[order_id] = order
    return order


def find_order(order_id):
    return orders.get(order_id)
