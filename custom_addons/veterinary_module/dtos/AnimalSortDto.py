from typing import Dict
import json
from custom_addons.veterinary_module.common.bases.dtos import BaseDto


class AnimalSortDto(BaseDto):
    sort_name: str

    def __init__(self, id: int, sort_name: str) -> None:
        super().__init__(id)
        self.sort_name: str = sort_name

    def to_dict(self) -> Dict[str, str | int]:
        base = super().to_dict()
        base.update({"sort_name": self.sort_name})
        return base

    @staticmethod
    def from_dict(data: dict) -> "AnimalSortDto":
        orders_data = data.get("animal_sorts", [])
        orders = [AnimalSortDto.from_dict(o) for o in orders_data]
        return AnimalSortDto(
            id=data.get("id"),
            sort_name=data.get("sort_name")
        )

    def to_json(self):
        return json.dumps(self.to_dict())