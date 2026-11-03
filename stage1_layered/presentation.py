# PRESENTATION LAYER: receives requests and returns (status code, body).
#
# STARTING POINT: this file still does everything, exactly like stage 0:
# it checks the input, applies the shop rules AND stores the data.
# In step 3 it will only call business.py and turn errors into status codes.

import business

# mapping of errors
# 
# InvalidData -> 400
# NotFound -> 404
# NotEnoughStock -> 409

class ShopAPI:
    def _call(self, status, fn, *args):
        try:
            return status, fn(*args)
        except business.InvalidData as error:
            return 400, {"error": str(error)}
        except business.NotFound as error:
            return 404, {"error": str(error)}
        except business.NotEnoughStock as error:
            return 409, {"error": str(error)}
        except Exception as error:
            return 500, {"error": str(error)}

    def add_book(self, request):
        title = request.get("title")
        price_cents = request.get("price_cents")
        stock = request.get("stock")
        return self._call(201, business.add_book, title, price_cents, stock)

    def list_books(self):
        return self._call(200, business.list_books)

    def place_order(self, request):
        book_id = request.get("book_id")
        quantity = request.get("quantity")

        return self._call(201, business.place_order, book_id, quantity)
        
    def get_order(self, order_id):
        return self._call(200, business.get_order, order_id)
