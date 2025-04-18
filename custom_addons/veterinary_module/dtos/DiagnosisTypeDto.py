import json
from typing import Dict, List

from custom_addons.veterinary_module.common.bases.dtos import BaseDto
from odoo.fields import Datetime


class DiagnosisTypeDto(BaseDto):

    def __init__(self, id: int, description: str, sort_name: str,
                 create_date:Datetime, write_date:Datetime) -> None:
        super().__init__(id, create_date, write_date)
        self.sort_name: str = sort_name
        self.description:str = description

    def to_dict(self) -> Dict[str, str | int | Datetime]:
        base = super().to_dict()
        base.update({"sort_name": self.sort_name})
        base.update({"description": self.description})
        return base

    @staticmethod
    def from_dict(data: dict) -> "DiagnosisTypeDto":
        return DiagnosisTypeDto(
            id=data.get("id"),
            create_date=data.get("create_date"),
            write_date=data.get("write_date"),
            description=data.get("description"),
            sort_name=data.get("sort_name"),
        )

    def to_json(self):
        return json.dumps(self.to_dict())