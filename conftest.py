import httpx
import pytest
from api.orders_api import OrdersApi
from data.order_factory import make_order_data


BASE_URL = "https://petstore.swagger.io/v2" #вынести в .env

@pytest.fixture(scope="session")
def http_client():
    with httpx.Client(
        base_url="https://petstore.swagger.io/v2",
        headers={"Accept": "application/json"},
        timeout=15.0,
    ) as client:
        yield client

@pytest.fixture(scope="session")
def orders_api(http_client):
    return OrdersApi(http_client)

@pytest.fixture(scope="function")
def order_data():
    return make_order_data()