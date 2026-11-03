# CATALOG - PERSISTENCE: stores and finds books. Only the catalog domain uses it.

books: dict[int, dict] = {}


def reset() -> None:
    books.clear()


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
