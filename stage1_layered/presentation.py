# PRESENTATION LAYER: receives requests and returns (status code, body).
# It only calls the business layer and turns its errors into status codes.

import business
from business import InvalidData, NotEnoughStock, NotFound, ShopError

STATUS_CODES = {
    InvalidData   : 400,
    NotFound      : 404,
    NotEnoughStock: 409,
}


class ShopAPI:
    def add_book(self, request: dict) -> tuple[int, dict]:
        try:
            book = business.add_book(
                request.get('title'),
                request.get('price_cents'),
                request.get('stock'),
            )
        except ShopError as error:
            return STATUS_CODES[type(error)], {'error': str(error)}
        return 201, book

    def list_books(self) -> tuple[int, list[dict]]:
        return 200, business.list_books()

    def place_order(self, request: dict) -> tuple[int, dict]:
        try:
            order = business.place_order(
                request.get('book_id'),
                request.get('quantity'),
            )
        except ShopError as error:
            return STATUS_CODES[type(error)], {'error': str(error)}
        return 201, order

    def get_order(self, order_id: int) -> tuple[int, dict]:
        try:
            order = business.get_order(order_id)
        except ShopError as error:
            return STATUS_CODES[type(error)], {'error': str(error)}
        return 200, order
