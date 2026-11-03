# CATALOG - BUSINESS: the rules about books and stock.
# This is also the only part of the catalog that other domains may use.

from catalog import persistence
from errors import InvalidData, NotEnoughStock, NotFound


def add_book(title, price_cents, stock):
    # TODO step 1: move the code from the old business.py here
    if not isinstance(title, str) or not title:
        raise InvalidData("title must be a non-empty string")
    if not isinstance(price_cents, int) or price_cents <= 0:
        raise InvalidData("price_cents must be a positive integer")
    if not isinstance(stock, int) or stock < 0:
        raise InvalidData("stock must be a non-negative integer")
    return persistence.save_book(title, price_cents, stock)


def list_books():
    # TODO step 1: move the code from the old business.py here
    return persistence.all_books()


def get_price(book_id):
    # TODO step 1: new function. Return the price of the book, or raise NotFound
    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound(f"book {book_id} does not exist")
    return book["price_cents"]


def take_stock(book_id, quantity):
    # TODO step 1: new function. The stock check and update that were in place_order:
    #   raise NotFound or NotEnoughStock, otherwise subtract quantity from the stock
    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound(f"book {book_id} does not exist")
    if book["stock"] < quantity:
        raise NotEnoughStock(f"only {book['stock']} in stock")
    persistence.update_stock(book_id, book["stock"] - quantity)
