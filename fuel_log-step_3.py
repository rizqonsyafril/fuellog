# === Stage 3: Хранилище в памяти ===
# Project: FuelLog
from datetime import date


class TankingError(Exception):
    """Ошибка при работе с записями о заправках."""


class TankingRecord:
    """Запись о заправке: дата, объём, цена и пробег."""

    def __init__(self, date, liters, price, mileage):
        self.date = date
        self.liters = liters
        self.price = price
        self.mileage = mileage

    def to_dict(self):
        return {
            "date": self.date,
            "liters": self.liters,
            "price": self.price,
            "mileage": self.mileage,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            date=data["date"],
            liters=data["liters"],
            price=data["price"],
            mileage=data["mileage"],
        )

    def __repr__(self):
        return (
            "TankingRecord(date=%r, liters=%r, price=%r, mileage=%r)"
            % (self.date, self.liters, self.price, self.mileage)
        )


class TankingStore:
    """Хранилище записей о заправках в памяти."""

    def __init__(self):
        self._records = {}
        self._counter = 0

    def add(self, record):
        self._counter += 1
        record_id = self._counter
        self._records[record_id] = record
        return record_id

    def get(self, record_id):
        if record_id not in self._records:
            raise TankingError("Запись с идентификатором %r не найдена" % record_id)
        return self._records[record_id]

    def list(self):
        return list(self._records.values())
