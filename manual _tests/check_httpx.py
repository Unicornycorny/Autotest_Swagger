import httpx
from models.order_model import OrderResponse

order_data = {
    "id": 123,
    "petId": 456,
    "quantity": 2,
    "shipDate": "2026-11-01T12:00:00.000+0000",
    "status": "approved",
    "complete": True
}

with httpx.Client(
    base_url="https://petstore.swagger.io/v2",
    headers={"Accept": "application/json"},
    timeout=15.0
) as client:

    response = client.post(
        "/store/order",
        json=order_data
    )
    
response_data = response.json()

validated_order = OrderResponse.model_validate(response_data)

assert response.status_code == 200, (
    f"Expected status 200, got {response.status_code}"
)

print("Validated order:", validated_order)
print("ShipDate type:", type(validated_order.shipDate))
    
print("Status code:", response.status_code)
print("Response body:", response.text)
print("Request URL:", response.request.url)