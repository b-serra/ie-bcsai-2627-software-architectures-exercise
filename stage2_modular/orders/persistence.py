# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.

orders = {}

def reset():
    orders.clear()

def save_order(order):
    # TODO step 2: move the code from the old persistence.py here
    if not orders:
        order_id = 1
    else:
        order_id = max(orders.keys()) + 1
    order["id"] = order_id
    orders[order_id] = order
    return order

def find_order(order_id):
    # TODO step 2: move the code from the old persistence.py here
    return orders.get(order_id)
