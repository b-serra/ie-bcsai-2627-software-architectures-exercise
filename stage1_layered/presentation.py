# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.

import business

ERROR_STATUS: dict[type[business.ShopError], int] = {
    business.InvalidData: 400,
    business.NotFound: 404,
    business.NotEnoughStock: 409,
}


def _handle(success_status, action, *args):
    try:
        return success_status, action(*args)
    except business.ShopError as error:
        status = ERROR_STATUS.get(type(error), 400)
        return status, {"error": type(error).__name__}


class ShopAPI:
    def add_book(self, request):
        return _handle(
            201,
            business.add_book,
            request.get("title"),
            request.get("price_cents"),
            request.get("stock"),
        )

    def list_books(self):
        return _handle(200, business.list_books)

    def place_order(self, request):
        return _handle(
            201,
            business.place_order,
            request.get("book_id"),
            request.get("quantity"),
        )

    def get_order(self, order_id):
        return _handle(200, business.get_order, order_id)
