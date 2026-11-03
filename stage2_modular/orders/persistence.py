# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.

orders = {}


def reset():
    orders.clear()


def save_order(order):
    # TODO step 2: move the code from the old persistence.py here
    saved_order = {**order, "id": len(orders) + 1}
    orders[saved_order["id"]] = saved_order
    return saved_order


def find_order(order_id):
    # TODO step 2: move the code from the old persistence.py here
    return orders.get(order_id)
