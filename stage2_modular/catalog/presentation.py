# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request):
    # TODO step 1: move the code from the old presentation.py here
    title = request.get("title")
    price = request.get("price_cents")
    stock = request.get("stock")
    try:
        book = business.add_book(title, price, stock)
    except ShopError as error:
        return error_response(error)
    return 201, book


def list_books():
    # TODO step 1: move the code from the old presentation.py here
    return 200, business.list_books()
