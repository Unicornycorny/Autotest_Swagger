Для полного запуска выполните из корня проекта:

`.\run_tests.cmd`

Сценарий автоматически выполняет два теста, сохраняет результаты в `allure-results/` и генерирует HTML-отчёт в `allure-report/`.

`tests\test_store_order_httpx.py` - основной тест
`models\corder_model.py` - модель
`data\order_model.py` - генерируем данные, чтобы не одну и ту же структуру тестировать
`api\orders_api.py` - киадем запрос
`conftest.py` - собираем фикстуры

### Просмотр Allure-отчёта

После выполнения сценария откройте отчёт командой:

`allure.cmd open allure-report/awesome`

## Скриншоты Allure Report

### Общая статистика

![Allure Report — общая статистика](screenshots/1.png)