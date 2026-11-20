# === Stage 4: Удаление и восстановление ===
# Project: FuelLog
import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional


@dataclass
class FuelStation:
    date: datetime.date
    liters: float
    price: float
    mileage: float
    deleted: bool = False
    deleted_at: Optional[datetime.datetime] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "FuelStation":
        return cls(
            date=datetime.date.fromisoformat(data["date"]),
            liters=float(data["liters"]),
            price=float(data["price"]),
            mileage=float(data["mileage"]),
            deleted=bool(data.get("deleted", False)),
            deleted_at=None if data.get("deleted_at") is None else datetime.datetime.fromisoformat(data["deleted_at"]),
        )


class FuelStationRepository:
    def __init__(self):
        self._records: List[FuelStation] = []

    def add(self, station: FuelStation) -> None:
        self._records.append(station)

    def get_all(self) -> List[FuelStation]:
        return [s for s in self._records if not s.deleted]

    def get_trash(self) -> List[FuelStation]:
        return [s for s in self._records if s.deleted]

    def get(self, station: FuelStation) -> Optional[FuelStation]:
        for record in self._records:
            if record.id == station.id:
                return record
        return None

    def remove(self, station: FuelStation) -> None:
        record = self.get(station)
        if record is None:
            raise ValueError(f"Заправка {station.id} не найдена")
        record.deleted = True
        record.deleted_at = datetime.datetime.now()

    def restore(self, station: FuelStation) -> None:
        record = self.get(station)
        if record is None:
            raise ValueError(f"Заправка {station.id} не найдена")
        record.deleted = False
        record.deleted_at = None

    def permanent_delete(self, station: FuelStation) -> None:
        record = self.get(station)
        if record is None:
            raise ValueError(f"Заправка {station.id} не найдена")
        self._records.remove(record)


if __name__ == "__main__":
    repo = FuelStationRepository()
    s1 = FuelStation(date=datetime.date(2024, 1, 1), liters=40.0, price=55.0, mileage=1000)
    s2 = FuelStation(date=datetime.date(2024, 1, 15), liters=50.0, price=60.0, mileage=1500)
    repo.add(s1)
    repo.add(s2)
    print("Все заправки:", repo.get_all())
    repo.remove(s1)
    print("После удаления:", repo.get_all())
    print("В корзине:", repo.get_trash())
    repo.restore(s1)
    print("После восстановления:", repo.get_all())
    repo.perman
