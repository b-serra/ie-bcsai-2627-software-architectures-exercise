# CATALOG - BUSINESS: the rules about books and stock.
# This is also the only part of the catalog that other domains may use.

from catalog import persistence
from errors import InvalidData, NotEnoughStock, NotFound


def add_book(title, price_cents, stock):
    if type(title) != str or title == "":
        raise InvalidData
    if type(price_cents) != int or price_cents <= 0:
        raise InvalidData
    if type(stock) != int or stock < 0:
        raise InvalidData
    return persistence.save_book(title, price_cents, stock)

def list_books():
    return list(persistence.all_books())


def get_price(book_id):
    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound
    return book['price_cents']


def take_stock(book_id, quantity):
    book = persistence.find_book(book_id)
    if book is None:
        raise NotFound
    if book["stock"] < quantity:
        raise NotEnoughStock
    return persistence.update_stock(book_id, book["stock"] - quantity)
