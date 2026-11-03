# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request):
    try:
        book_id = request.get("book_id")
        quantity = request.get("quantity")
        order = business.place_order(book_id, quantity)
        return 201, order
    except ShopError as e:
        return error_response(e)


def get_order(order_id):
    try:
        order = business.get_order(order_id)
        return 200, order
    except ShopError as e:
        return error_response(e)
