# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request):
    # TODO step 1: move the code from the old presentation.py here
    if type(request) != dict:
        raise ShopError("request must be a dict")
    title = request.get("title")
    price_cents = request.get("price_cents")
    stock = request.get("stock")
    book = business.add_book(title, price_cents, stock)
    return 201, book


def list_books():
    # TODO step 1: move the code from the old presentation.py here
    books = business.list_books()
    return 200, books
