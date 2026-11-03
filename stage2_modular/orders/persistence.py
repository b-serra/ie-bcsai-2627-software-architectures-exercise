orders = {}


def reset():
    orders.clear()


def save_order(order):
    new_id = len(orders) + 1
    order["id"] = new_id
    orders[new_id] = order
    return order


def find_order(order_id):
    if order_id in orders:
        return orders[order_id]
    return None
