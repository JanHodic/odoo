import json
from typing import Dict, List

from custom_addons.veterinary_module.common.bases.dtos import BaseDto
from custom_addons.veterinary_module.dtos.DiagnosisTypeDto import DiagnosisTypeDto
from custom_addons.veterinary_module.dtos.TreatmentDto import TreatmentDto
from odoo.fields import Datetime


class DiagnosisDto(BaseDto):

    def __init__(self, id: int, cured: bool, type: DiagnosisTypeDto, description: str, treatments: List[TreatmentDto],
                 create_date:Datetime, write_date:Datetime) -> None:
        super().__init__(id, create_date, write_date)
        self.cured: bool = cured
        self.type:DiagnosisTypeDto = type
        self.description:str = description
        self.treatments:List[TreatmentDto] = treatments

    def to_dict(self) -> Dict[str, str | int | Datetime]:
        base = super().to_dict()
        base.update({"cured": self.cured})
        base.update({"type": self.type})
        base.update({"description": self.description})
        base.update({"treatments": self.treatments})
        return base

    @staticmethod
    def from_dict(data: dict) -> "DiagnosisDto":
        return DiagnosisDto(
            id=data.get("id"),
            create_date=data.get("create_date"),
            write_date=data.get("write_date"),
            cured=data.get("cured"),
            type=data.get("type"),
            description=data.get("description"),
            treatments=data.get("treatments"),
        )

    def to_json(self):
        return json.dumps(self.to_dict())