
import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_create_order_status_200():
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
        headers={"Accept": "application/json"}, #формат ответа 
        timeout=15
    )

    print("HTTP status:", response.status_code)
    print("Response body:", response.text)

    assert response.status_code == 200, (
        f"Expected 200, but got {response.status_code}. "
        f"Response: {response.text}"
    )
