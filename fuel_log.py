# === Stage 1: Каркас модуля ===
# Project: FuelLog
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Refueling:
    date: date
    liters: float
    price: float
    mileage: float

    @property
    def cost(self) -> float:
        return self.liters * self.price


def create_demo_records() -> list[Refueling]:
    return [
        Refueling(date(2024, 1, 5), 40.0, 45.5, 10000),
        Refueling(date(2024, 1, 20), 38.0, 46.0, 15000),
        Refueling(date(2024, 2, 10), 42.0, 45.0, 22000),
    ]


def main() -> None:
    records = create_demo_records()
    print("FuelLog - демо-данные")
    print(f"Записей заливок: {len(records)}")
    for r in records:
        print(f"{r.date} | {r.liters} л | {r.cost:.2f} руб | пробег {r.mileage}")


if __name__ == "__main__":
    main()
