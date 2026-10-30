from models.order_model import OrderResponse
import pytest
import allure
from utils.allure_helpers import attach_http_data

@allure.feature("Store")
@allure.story("Create order")
@allure.title("POST /store/order — HTTP status 200")
@pytest.mark.smoke
def test_create_order_status(orders_api, order_data):
    with allure.step("Отправить POST-запрос"):
        response = orders_api.create_order(order_data)
        attach_http_data(response)
    with allure.step("Проверить HTTP-статус 200"):
        assert response.status_code == 200 #response.raise_for_status() - проверяет на 2xx

@allure.feature("Store")
@allure.story("Create order")
@allure.title("POST /store/order — Contract validation")
@pytest.mark.contract
def test_create_order_contract(orders_api, order_data):
    with allure.step("Отправить POST-запрос"):
        response = orders_api.create_order(order_data)
        attach_http_data(response)
    with allure.step("Проверить HTTP-статус 200"):
        assert response.status_code == 200
    with allure.step("Проверить контракт ответа через Pydantic"):
        OrderResponse.model_validate(response.json())