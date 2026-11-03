# CATALOG - BUSINESS: the rules about books and stock.
# This is also the only part of the catalog that other domains may use.

from catalog import persistence
from errors import InvalidData, NotEnoughStock, NotFound


def add_book(title: str, price_cents: int, stock: int) -> dict:
    if type(title) is not str or title == '':
        raise InvalidData('title is required')
    if type(price_cents) is not int or price_cents <= 0:
        raise InvalidData('price must be a positive integer')
    if type(stock) is not int or stock < 0:
        raise InvalidData('stock cannot be negative')

    return persistence.save_book(title, price_cents, stock)


def list_books() -> list[dict]:
    return persistence.all_books()


def get_price(book_id: int) -> int:
    return _find_book(book_id)['price_cents']


def take_stock(book_id: int, quantity: int) -> None:
    book = _find_book(book_id)
    if book['stock'] < quantity:
        raise NotEnoughStock('not enough stock')

    persistence.update_stock(book_id, book['stock'] - quantity)


def _find_book(book_id: int) -> dict:
    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound('book not found')
    return book
