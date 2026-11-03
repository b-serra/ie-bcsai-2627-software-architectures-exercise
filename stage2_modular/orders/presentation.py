# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request):
    # TODO step 2: move the code from the old presentation.py here
    book_id = request.get("book_id")
    quantity = request.get("quantity")
    try:
        order = business.place_order(book_id, quantity)
    except ShopError as error:
        return error_response(error)
    return 201, order


def get_order(order_id):
    # TODO step 2: move the code from the old presentation.py here
    try:
        order = business.get_order(order_id)
    except ShopError as error:
        return error_response(error)
    return 200, order
