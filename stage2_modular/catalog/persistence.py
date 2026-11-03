# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    book = {"id": len(books) + 1, "title": title, "price_cents": price_cents, "stock": stock}
    books[book["id"]] = book
    return book


def find_book(book_id):
    return books.get(book_id)


def all_books():
    return list(books.values())


def update_stock(book_id, new_stock):
    books[book_id]["stock"] = new_stock