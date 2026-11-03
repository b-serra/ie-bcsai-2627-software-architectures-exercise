# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.

orders = {}


def reset():
    orders.clear()


def save_order(order):
    # TODO step 1: give the order the next id, store it in `orders` and return it
    order_id = len(orders) + 1
    order["id"] = order_id
    orders[order_id] = order
    return order


def find_order(order_id):
    # TODO step 1: return the order, or None if it does not exist
    return orders.get(order_id)
