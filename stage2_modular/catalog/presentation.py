# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request):
    try:
        return 201, business.add_book(request.get("title"), request.get("price_cents"), request.get("stock"))
    except ShopError as error:
        return error_response(error)

def list_books():
    return 200, business.list_books()

def place_order(request):
    try:
        return 201, business.place_order(request.get("book_id"), request.get("quantity"))
    except ShopError as error:
        return error_response(error)

def get_order(order_id):
    try:
        return 200, business.get_order(order_id)
    except ShopError as error:
        return error_response(error)
