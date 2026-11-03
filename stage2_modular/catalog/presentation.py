# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request):
    # TODO step 1: move the code from the old presentation.py here
    try:
        return 201, business.add_book(request.get("title"), request.get("price_cents"), request.get("stock"))
    except ShopError as error:
        return error_response(error)


def list_books():
    # TODO step 1: move the code from the old presentation.py here
    return 200, business.list_books()
