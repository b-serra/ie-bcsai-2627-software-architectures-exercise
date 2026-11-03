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
        return 201, book
    
    except business.InvalidData as e:
        return 400, {"error": str(e)}


def list_books():
    # TODO step 1: move the code from the old presentation.py here
    try: 
        books = business.list_books()
        return 200, books
    except Exception as e:
        return 500, {"error": str(e)}
