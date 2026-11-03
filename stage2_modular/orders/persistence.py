# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.

orders = {}


def reset():
    orders.clear()


def save_order(order):
    # TODO step 2: move the code from the old persistence.py here
    order["id"] = len(orders) + 1
    orders[order["id"]] = order
    return order


def find_order(order_id):
    # TODO step 2: move the code from the old persistence.py here
    return orders.get(order_id)
