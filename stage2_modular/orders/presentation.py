# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request):
    # TODO step 2: move the code from the old presentation.py here
    try:
        order = business.place_order(request.get("book_id"), request.get("quantity"))
    except business.InvalidData:
        return 400, {"error": "book_id and a positive quantity are required"}
    except business.NotFound:
        return 404, {"error": "book not found"}
    except business.NotEnoughStock:
        return 409, {"error": "not enough stock"}
    return 201, order


def get_order(order_id):
    try:
        order = business.get_order(order_id)
    except business.NotFound:
        return 404, {"error": "order not found"}
    return 200, order
    # TODO step 2: move the code from the old presentation.py here
