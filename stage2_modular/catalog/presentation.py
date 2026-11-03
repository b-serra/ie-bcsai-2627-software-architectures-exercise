# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request):
    try:
        title = request.get("title")
        price = request.get("price_cents")
        stock = request.get("stock")
        book = business.add_book(title, price, stock)
        return 201, book
    except business.InvalidData as e:
        return 400, {"error": str(e)}


def list_books():
    return 200, business.list_books()
