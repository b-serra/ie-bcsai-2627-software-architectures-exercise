orders = {}


def reset():
    orders.clear()


def save_order(order):
    order["id"] = len(orders) + 1
    orders[order["id"]] = order
    return order


def find_order(order_id):
    return orders.get(order_id)