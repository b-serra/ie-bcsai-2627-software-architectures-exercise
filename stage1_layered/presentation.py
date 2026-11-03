import business


def error_response(error):
    codes = {
        business.InvalidData: 400,
        business.NotFound: 404,
        business.NotEnoughStock: 409,
    }
    return codes[type(error)], {"error": str(error)}


class ShopAPI:
    def add_book(self, request):
        try:
            book = business.add_book(
                request.get("title"),
                request.get("price_cents"),
                request.get("stock"),
            )
            return 201, book
        except business.ShopError as error:
            return error_response(error)

    def list_books(self):
        return 200, business.list_books()

    def place_order(self, request):
        try:
            order = business.place_order(
                request.get("book_id"), request.get("quantity")
            )
            return 201, order
        except business.ShopError as error:
            return error_response(error)

    def get_order(self, order_id):
        try:
            return 200, business.get_order(order_id)
        except business.ShopError as error:
            return error_response(error)