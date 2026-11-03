# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request: dict) -> tuple[int, dict]:
    try:
        order = business.place_order(
            request.get('book_id'),
            request.get('quantity'),
        )
    except ShopError as error:
        return error_response(error)
    return 201, order


def get_order(order_id: int) -> tuple[int, dict]:
    try:
        order = business.get_order(order_id)
    except ShopError as error:
        return error_response(error)
    return 200, order
