# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: move the code from the old persistence.py here
    book = {"id": len(books) + 1, "title": title, "price_cents": price_cents, "stock": stock}
    books[book["id"]] = book
    print("Added book " + title)
    return book

def find_book(book_id):
    # TODO step 1: move the code from the old persistence.py here
    if book_id in books:
        return books[book_id]
    return None


def all_books():
    # TODO step 1: move the code from the old persistence.py here
    return list(books.values())


def update_stock(book_id, new_stock):
    # TODO step 1: move the code from the old persistence.py here
    book = find_book(book_id)
    if book:
        book["stock"] = new_stock
        return True
    return False
