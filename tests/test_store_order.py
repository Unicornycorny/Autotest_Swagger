
import json
from pathlib import Path

import allure
import pytest
import requests
from jsonschema import validate, FormatChecker, ValidationError


BASE_URL = "https://petstore.swagger.io/v2"

SCHEMA_PATH = (
    Path(__file__).resolve().parents[1] #Path(_file_) - объект пути, _file_ - пусть к исполняемому файлу
    / "schemas"
    / "order_schema.json"
)


@pytest.fixture(scope="module") #декоратор фикстура
def order_response():
    order_data = {
        "id": 12345,
        "petId": 123,
        "quantity": 2,
        "shipDate": "2026-11-01T12:00:00.000Z",
        "status": "placed",
        "complete": False
    }

    response = requests.post(
        url=f"{BASE_URL}/store/order",
        json=order_data,
        headers={"Accept": "application/json"},
        timeout=15
    )

    print("Response status:", response.status_code)
    print("Response body:", response.text)

    return response #передаёт результат 1 раз каждому тесту, а не при вызове


# Вдобавление данных в Allure
def attach_http_data(response):

    with allure.step("Сохранить HTTP-запрос и ответ"):

        allure.attach(
            response.request.body or "",
            name="Request Body",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            f"URL: {response.request.url}\n"
            f"Status: {response.status_code}",
            name="HTTP Information",
            attachment_type=allure.attachment_type.TEXT
        )


#проверка статуса
@allure.feature("Store")
@allure.story("Create order")
@allure.title("POST /store/order - HTTP status 200")
def test_create_order_status_200(order_response):

    attach_http_data(order_response)

    with allure.step("Проверить HTTP-статус 200"):
        assert order_response.status_code == 200, (
            f"Expected 200, got {order_response.status_code}. "
            f"Response: {order_response.text}"
        )


#проверка модели
@allure.feature("Store")
@allure.story("Create order")
@allure.title("POST /store/order - Response schema validation")
def test_create_order_schema(order_response):

    attach_http_data(order_response)

    with allure.step("Преобразовать ответ в JSON"):
        response_body = order_response.json() # Преобразование JSON в словарь Python

    with allure.step("Загрузить JSON Schema модели Order"):

        # Загрузка JSON Schema из файла
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            order_schema = json.load(schema_file) #в словарь python

    with allure.step("Проверить структуру, типы и форматы"):
        try:
            validate(
                instance=response_body,
                schema=order_schema,
                format_checker=FormatChecker()
            )

        except ValidationError as error:
            field = ".".join(
                str(part) for part in error.absolute_path
            )

            pytest.fail(
                f"Schema validation failed at "
                f"'{field or '<root>'}': {error.message}",
                pytrace=False #не выводить трассировку в консоль
            )
