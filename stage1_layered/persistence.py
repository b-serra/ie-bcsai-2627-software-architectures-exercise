# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: create the book dict with the next id, store it in `books` and return it
    next_id = max(books.keys(), default=0) + 1
    books[next_id] = {"id": next_id, "title": title, "price_cents": price_cents, "stock": stock}
    print("Added book " + title)
    return books[next_id]



def find_book(book_id):
    # TODO step 1: return the book, or None if it does not exist
    if book_id in books:
        return books[book_id]
    else:
        return None


def all_books():
    # TODO step 1: return a list with all the books
    return list(books.values())


def update_stock(book_id, new_stock):
    # TODO step 1: change the stock of the book
    books[book_id]["stock"] = new_stock
    return books[book_id]


def save_order(order):
    # TODO step 1: give the order the next id, store it in `orders` and return it
    next_id = max(orders.keys(), default=0) + 1
    order = {"id": next_id, **order}
    orders[next_id] = order
    return order


def find_order(order_id):
    # TODO step 1: return the order, or None if it does not exist
    if order_id in orders:
        return orders[order_id]
    else:
        return None
