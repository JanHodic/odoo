import json
from typing import Dict, List

from custom_addons.veterinary_module.common.bases.dtos import BaseDto
from custom_addons.veterinary_module.dtos.MedicalDto import MedicalDto
from odoo.fields import Datetime


class TreatmentDto(BaseDto):

    def __init__(self, id: int, date_time: Datetime, realised: bool, description: str, medicals: List[MedicalDto],
                 create_date:Datetime, write_date:Datetime) -> None:
        super().__init__(id, create_date, write_date)
        self.date_time: Datetime = date_time
        self.realised:bool = realised
        self.description:str = description
        self.medicals:List[MedicalDto] = medicals

    def to_dict(self) -> Dict[str, str | int | Datetime]:
        base = super().to_dict()
        base.update({"date_time": self.date_time})
        base.update({"realised": self.realised})
        base.update({"description": self.description})
        base.update({"medicals": self.medicals})
        return base

    @staticmethod
    def from_dict(data: dict) -> "MedicalDto":
        return MedicalDto(
            id=data.get("id"),
            create_date=data.get("create_date"),
            write_date=data.get("write_date"),
            realised=data.get("realised"),
            date_time=data.get("date_time"),
            description=data.get("description"),
            medicals=data.get("medicals"),
        )

    def to_json(self):
        return json.dumps(self.to_dict())