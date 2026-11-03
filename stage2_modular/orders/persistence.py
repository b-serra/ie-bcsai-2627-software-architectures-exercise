# ORDERS - PERSISTENCE: stores and finds orders. Only the orders domain uses it.

orders: dict[int, dict] = {}


def reset() -> None:
    orders.clear()


def save_order(order: dict) -> dict:
    saved = {
        'id': len(orders) + 1,
        **order,
    }
    orders[saved['id']] = saved
    return saved


def find_order(order_id: int) -> dict | None:
    return orders.get(order_id)
