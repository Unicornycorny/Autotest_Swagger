import httpx
import allure

# Добавление данных в Allure
def attach_http_data(response: httpx.Response) -> None:
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.TEXT
    )
    
    allure.attach(
    response.request.content.decode("utf-8"),
    name="Request body",
    attachment_type=allure.attachment_type.JSON
    )
    
    allure.attach(
    f"Method: {response.request.method}\n"
    f"URL: {response.request.url}\n"
    f"Status: {response.status_code}",
    name="HTTP info",
    attachment_type=allure.attachment_type.TEXT
)