# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: move the code from the old persistence.py here
    book_id = len(books) + 1
    book = {"id": book_id, "title": title, "price_cents": price_cents, "stock": stock}
    books[book_id] = book
    return book


def find_book(book_id):
    # TODO step 1: move the code from the old persistence.py here
    return books.get(book_id)


def all_books():
    # TODO step 1: move the code from the old persistence.py here
    return list(books.values())


def update_stock(book_id, new_stock):
    # TODO step 1: move the code from the old persistence.py here
    books[book_id]["stock"] = new_stock
