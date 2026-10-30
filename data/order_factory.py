#чтобы вызывать order_data = make_order_data(),то есть создание тестовых данных,
# хотим проверять случайные данные, а не фиксированный словарь
from datetime import datetime, timedelta, timezone
from secrets import randbelow, randbits


def make_order_data() -> dict:
    order_id = randbelow(1_000_000_000) + 1

    ship_date = (
        datetime.now(timezone.utc) + timedelta(days=1)
    ).isoformat(timespec="milliseconds")

    return {
        "id": order_id,
        "petId": randbelow(1_000_000_000) + 1,
        "quantity": 1,
        "shipDate": ship_date,
        "status": "placed",
        "complete": False
    }