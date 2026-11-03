# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.


orders = {}

def reset():
    orders.clear()

def save_order(order):
    order_id = len(orders) + 1
    order["id"] = order_id
    orders[order_id] = order
    return order

def find_order(order_id):
    return orders.get(order_id)
