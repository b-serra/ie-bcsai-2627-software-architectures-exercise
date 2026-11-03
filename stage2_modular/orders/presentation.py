# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request):
    # TODO step 2: move the code from the old presentation.py here
    if type(request) != dict:
        raise ShopError("request must be a dict")
    book_id = request.get("book_id")
    quantity = request.get("quantity")
    order = business.place_order(book_id, quantity)
    return 201, order


def get_order(order_id):
    # TODO step 2: move the code from the old presentation.py here
    if type(order_id) != int:
        raise ShopError("order_id must be an int")
    order = business.get_order(order_id)
    return 200, order
