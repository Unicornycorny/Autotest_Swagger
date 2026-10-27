
import json
from pathlib import Path
from urllib import response

import pytest
import requests
from jsonschema import validate, FormatChecker


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

#проверка статуса
def test_create_order_status_200(order_response): 
    assert order_response.status_code == 200, (
        f"Expected 200, got {order_response.status_code}. "
        f"Response: {order_response.text}"
    )
    
    
    #проверка модели
def test_create_order_schema(order_response):
        response_body = order_response.json() # Преобразование JSON в словарь Python

        # Загрузка JSON Schema из файла
        with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
            order_schema = json.load(schema_file) #в словарь python

        validate(
            instance=response_body,
            schema=order_schema,
            format_checker=FormatChecker()
        )
