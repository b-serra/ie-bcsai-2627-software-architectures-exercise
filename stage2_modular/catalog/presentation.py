# CATALOG - PRESENTATION: book requests in, (status code, body) out.

from catalog import business
from errors import ShopError, error_response


def add_book(request: dict) -> tuple[int, dict]:
    try:
        book = business.add_book(
            request.get('title'),
            request.get('price_cents'),
            request.get('stock'),
        )
    except ShopError as error:
        return error_response(error)
    return 201, book


def list_books() -> tuple[int, list[dict]]:
    return 200, business.list_books()
