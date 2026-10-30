def test_order_data_first(order_data):
    print("First test ID:", order_data["id"])

    assert isinstance(order_data, dict)
    assert "shipDate" in order_data

def test_order_data_second(order_data):
    print("Second test ID:", order_data["id"])
    assert "petId" in order_data