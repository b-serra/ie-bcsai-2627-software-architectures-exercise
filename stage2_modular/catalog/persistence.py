# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    id = len(books) + 1
    books[id] = {'id': id, "title": title, "price_cents": price_cents, "stock": stock}
    return books[id]


def find_book(book_id):
    return books.get(book_id)


def all_books():
    return books.values()


def update_stock(book_id, new_stock):
    if not books[book_id]:
        return None
    books[book_id]['stock'] = new_stock
    return books[book_id]
