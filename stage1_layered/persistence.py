# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}

def reset():
    books.clear()
    orders.clear()

def save_book(title, price_cents, stock):
    # TODO step 1: create the book dict with the next id, store it in `books` and return it
    if books:
        next_id = max(books.keys()) + 1
    else:
        next_id = 1
    book = {
        'id': next_id,
        'title': title,
        'price_cents': price_cents,
        'stock': stock
    }
    books[next_id] = book
    return book

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
    if book_id in books:
        books[book_id]['stock'] = new_stock
        return True
    else:
        return False

def save_order(order):
    # TODO step 1: give the order the next id, store it in `orders` and return it
    if orders:
        next_id = max(orders.keys()) + 1
    else:
        next_id = 1
    order['id'] = next_id
    orders[next_id] = order
    return order

def find_order(order_id):
    # TODO step 1: return the order, or None if it does not exist
    if order_id in orders:
        return orders[order_id]
    else:
        return None
