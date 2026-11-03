books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


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


def save_order(order):
    new_id = len(orders) + 1
    order["id"] = new_id
    orders[new_id] = order
    return order


def find_order(order_id):
    if order_id in orders:
        return orders[order_id]
    return None
