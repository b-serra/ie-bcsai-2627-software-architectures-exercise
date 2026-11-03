# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books : dict[int, dict] = {}
orders: dict[int, dict] = {}


def reset() -> None:
    books.clear()
    orders.clear()


def save_book(title: str, price_cents: int, stock: int) -> dict:
    book = {
        'id'         : len(books) + 1,
        'title'      : title,
        'price_cents': price_cents,
        'stock'      : stock,
    }
    books[book['id']] = book
    return book


def find_book(book_id: int) -> dict | None:
    return books.get(book_id)


def all_books() -> list[dict]:
    return list(books.values())


def update_stock(book_id: int, new_stock: int) -> None:
    books[book_id]['stock'] = new_stock


def save_order(order: dict) -> dict:
    saved = {
        'id': len(orders) + 1,
        **order,
    }
    orders[saved['id']] = saved
    return saved


def find_order(order_id: int) -> dict | None:
    return orders.get(order_id)
