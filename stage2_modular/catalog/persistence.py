# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    # TODO step 1: move the code from the old persistence.py here
    book = {"id": len(books) + 1, "title": title, "price_cents": price_cents, "stock": stock}
    books[book["id"]] = book
    return book    
    raise NotImplementedError("TODO step 1")


def find_book(book_id):
    # TODO step 1: move the code from the old persistence.py here
    if books.get(book_id, None) == None:
        return None
    else:
        return books[book_id]
    raise NotImplementedError("TODO step 1")


def all_books():
    # TODO step 1: move the code from the old persistence.py here
    return list(books.values())
    raise NotImplementedError("TODO step 1")


def update_stock(book_id, new_stock):
    # TODO step 1: move the code from the old persistence.py here
    books[book_id]["stock"] = new_stock
    raise NotImplementedError("TODO step 1")
