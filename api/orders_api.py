#класс OrdersApi - Его задача — знать,
# каким HTTP-методом и по какому адресу создавать заказ, но не проверять результат.

import httpx


class OrdersApi:
    def __init__(self, client: httpx.Client):
        self.client = client

    def create_order(self, order_data: dict) -> httpx.Response:
        return self.client.post("/store/order", json=order_data)

#response = orders_api.create_order(order_data)