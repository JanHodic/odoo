import json
from typing import Dict, List

from custom_addons.veterinary_module.common.bases.dtos import BaseDto
from custom_addons.veterinary_module.dtos.TreatmentDto import TreatmentDto
from odoo.fields import Datetime


class MedicalDto(BaseDto):

    def __init__(self, id: int, date_time: Datetime, description: str, treatments:List[TreatmentDto], create_date:Datetime, write_date:Datetime) -> None:
        super().__init__(id, create_date, write_date)
        self.date_time: str = date_time
        self.description: str = description
        self.treatments: List[TreatmentDto] = treatments

    def to_dict(self) -> Dict[str, str | int | Datetime]:
        base = super().to_dict()
        base.update({"date_time": self.date_time})
        base.update({"description": self.description})
        base.update({"treatments": self.treatments})
        return base

    @staticmethod
    def from_dict(data: dict) -> "MedicalDto":
        return MedicalDto(
            id=data.get("id"),
            date_time=data.get("date_time"),
            description=data.get("description"),
            treatments=data.get("treatments"),
        )

    def to_json(self):
        return json.dumps(self.to_dict())