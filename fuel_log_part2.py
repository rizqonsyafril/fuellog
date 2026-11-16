# === Stage 2: Проверка полей ===
# Project: FuelLog
from datetime import datetime


class FuelValidationError(Exception):
    pass


DATE_FORMAT = "%d.%m.%Y"


def parse_date(value):
    try:
        return datetime.strptime(value.strip(), DATE_FORMAT).date()
    except (ValueError, AttributeError):
        raise FuelValidationError("Дата должна быть в формате ДД.ММ.ГГГГ, например 15.06.2024.")


def parse_number(value, field_name, minimum=None, maximum=None):
    try:
        result = float(value.strip())
    except (ValueError, AttributeError):
        raise FuelValidationError(f"Поле «{field_name}» должно быть числом.")
    if result != result:
        raise FuelValidationError(f"Поле «{field_name}» не может быть пустым.")
    if minimum is not None and result < minimum:
        raise FuelValidationError(f"Поле «{field_name}» должно быть не меньше {minimum}.")
    if maximum is not None and result > maximum:
        raise FuelValidationError(f"Поле «{field_name}» должно быть не больше {maximum}.")
    return result


def normalize_fillup(date, liters, price, mileage):
    return {
        "date": parse_date(date),
        "liters": parse_number(liters, "литры", minimum=0.0001),
        "price": parse_number(price, "цена", minimum=0.01),
        "mileage": parse_number(mileage, "пробег", minimum=0.0),
    }
