# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

from errors import InvalidData, NotFound
books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: move the code from the old persistence.py here
    if type(title) != str or title == "":
        raise InvalidData("title is required")
    if type(price_cents) != int or price_cents <= 0:
        raise InvalidData("price must be a positive integer")
    if type(stock) != int or stock < 0:
        raise InvalidData("stock cannot be negative")
    book_id = len(books) + 1
    books[book_id] = {"id": book_id, "title": title, "price_cents": price_cents, "stock": stock}
    return books[book_id]

def find_book(book_id):
    # TODO step 1: move the code from the old persistence.py here
    if type(book_id) != int:
        raise InvalidData("book_id must be an integer")
    return books.get(book_id)


def all_books():
    # TODO step 1: move the code from the old persistence.py here
    return list(books.values())


def update_stock(book_id, new_stock):
    # TODO step 1: move the code from the old persistence.py here
    if type(book_id) != int:
        raise InvalidData("book_id must be an integer")
    if type(new_stock) != int:
        raise InvalidData("new_stock must be an integer")
    book = find_book(book_id)
    if book is None:
        raise NotFound("book not found")
    books[book_id] = {**book, "stock": new_stock}