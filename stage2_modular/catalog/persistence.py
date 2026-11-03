# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: move the code from the old persistence.py here
    book = {"id": len(books) + 1, "title": title, "price_cents": price_cents, "stock": stock}
    books[book["id"]] = book
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