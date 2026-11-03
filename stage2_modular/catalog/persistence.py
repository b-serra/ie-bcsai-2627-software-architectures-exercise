# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: create the book dict with the next id, store it in `books` and return it
    book_id = len(books) + 1
    book = {"id": book_id, "title": title, "price_cents": price_cents, "stock": stock}
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
