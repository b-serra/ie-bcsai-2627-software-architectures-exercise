# CATALOG - BUSINESS: the rules about books and stock.
# This is also the only part of the catalog that other domains may use.

from catalog import persistence
from errors import InvalidData, NotEnoughStock, NotFound


def add_book(title, price_cents, stock):
    # TODO step 1: move the code from the old business.py here
    if type(title) != str or title == "":
        raise InvalidData
    if type(price_cents) != int or price_cents <= 0:
        raise InvalidData
    if type(stock) != int or stock < 0:
        raise InvalidData
    return persistence.save_book(title, price_cents, stock)
    print("Added book " + title)     


def list_books():
    # TODO step 1: move the code from the old business.py here
    return persistence.all_books()
    raise NotImplementedError("TODO step 1")


def get_price(book_id):
    # TODO step 1: new function. Return the price of the book, or raise NotFound
    if persistence.books.get(book_id, None) == None:
        raise NotFound
    else:
        return persistence.books[book_id]["price_cents"]
    raise NotImplementedError("TODO step 1")


def take_stock(book_id, quantity):
    book = persistence.books.get(book_id, None)
    if book == None:
        raise NotFound
    elif quantity > book["quantity"]:
        raise NotEnoughStock
    else:
        book["quantity"] -= quantity
    # TODO step 1: new function. The stock check and update that were in place_order:
    #   raise NotFound or NotEnoughStock, otherwise subtract quantity from the stock
    raise NotImplementedError("TODO step 1")
