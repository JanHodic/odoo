from typing import Dict
import json
from custom_addons.veterinary_module.common.bases.dtos import BaseDto


class AnimalSortDto(BaseDto):
    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name: str = name

    def to_dict(self) -> Dict[str, str | int]:
        base = super().to_dict()
        base.update({"name": self.name})
        return base

    @staticmethod
    def from_dict(data: dict) -> "BaseDto":
        return BaseDto(
            id=data.get("id"),
            name=data.get("name")
        )

    def to_json(self):
        return json.dumps(self.to_dict())