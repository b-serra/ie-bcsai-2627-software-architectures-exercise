# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.

orders = {}


def reset():
    orders.clear()


def save_order(order):
    id = len(orders) + 1
    order['id'] = id
    orders[id] = order
    return orders[id]


def find_order(order_id):
    return orders.get(order_id)
