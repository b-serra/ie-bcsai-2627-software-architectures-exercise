books = {}


def reset():
    books.clear()


def save_book(title, price_cents, stock):
    new_id = len(books) + 1
    book = {"id": new_id, "title": title, "price_cents": price_cents, "stock": stock}
    books[new_id] = book
    return book


def find_book(book_id):
    if book_id in books:
        return books[book_id]
    return None


def all_books():
    return list(books.values())


def update_stock(book_id, new_stock):
    books[book_id]["stock"] = new_stock
