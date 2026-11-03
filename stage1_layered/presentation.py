# PRESENTATION LAYER: receives requests and returns (status code, body).

import business

STATUS = {business.InvalidData: 400, business.NotFound: 404, business.NotEnoughStock: 409}


class ShopAPI:
    def _call(self, status, function, *args):
        try:
            return status, function(*args)
        except business.ShopError as error:
            return STATUS[type(error)], {"error": str(error)}

    def add_book(self, request):
        return self._call(201, business.add_book, request.get("title"), request.get("price_cents"), request.get("stock"))

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        return self._call(201, business.place_order, request.get("book_id"), request.get("quantity"))

    def get_order(self, order_id):
        return self._call(200, business.get_order, order_id)
