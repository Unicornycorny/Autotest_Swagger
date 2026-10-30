def test_http_client_fixture(http_client):
    assert not http_client.is_closed
    assert http_client.base_url.host == "petstore.swagger.io"

def test_orders_api_fixture(orders_api, http_client):
    assert orders_api.client is http_client
    assert not orders_api.client.is_closed