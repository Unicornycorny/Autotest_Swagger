from models.order_model import OrderResponse

response_data = {
    "id": 123,
    "petId": 456,
    "quantity": 2,
    "shipDate": "2026-11-01T12:00:00.000+0000",
    "status": "approved",
    "complete": True
}

order = OrderResponse.model_validate(response_data)

print(order)
print(type(order.shipDate))