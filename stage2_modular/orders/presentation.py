# ORDERS - PRESENTATION: order requests in, (status code, body) out.

from errors import ShopError, error_response
from orders import business


def place_order(request):
    # TODO step 2: move the code from the old presentation.py here
    book_id = request.get("book_id")
    quantity = request.get("quantity")
    try:
        order = business.place_order(book_id, quantity)
        return 201, order
    except business.InvalidData as e:
        return 400, {"error": str(e)}
    except business.NotFound as e:
        return 404, {"error": str(e)}
    except business.NotEnoughStock as e:
        return 409, {"error": str(e)}

def get_order(order_id):
    # TODO step 2: move the code from the old presentation.py here
    try:
        order = business.get_order(order_id)
        return 200, order
    except business.NotFound as e:
        return 404, {"error": str(e)}
    return 404, {"error": "order not found"}
