import json
from typing import Dict

from custom_addons.veterinary_module.common.bases.dtos import BaseDto
from odoo.fields import Datetime


class AnimalDto(BaseDto):

    def __init__(self, id: int,
                 animal_name: str,
                 birth_date: Datetime,
                 patient_number: str,
                 sterilised: bool,
                 animal_sort: str,
                 diagnosis: str,
                 create_date:Datetime=None,
                 write_date:Datetime=None) -> None:
            super().__init__(id, create_date, write_date)
            self.animal_name:str = animal_name
            self.birth_date:Datetime = birth_date
            self.patient_number:str = patient_number
            self.sterilised:bool = sterilised
            self.animal_sort:str = animal_sort
            self.diagnosis:str = diagnosis

    @staticmethod
    def from_dict(data: dict) -> "AnimalDto":
            return AnimalDto(
                    id=data.get("id"),
                    create_date = data.get("create_date"),
                    write_date = data.get("write_date"),
                    animal_name=data.get("animal_name"),
                    birth_date=data.get("birth_date"),
                    patient_number=data.get("patient_number"),
                    sterilised=data.get("sterilised"),
                    animal_sort=data.get("animal_sort"),
                    diagnosis=data.get("diagnosis"),
            )

    def to_dict(self)->Dict[str, str | int | Datetime]:
            base = super().to_dict()
            base.update({"animal_name": self.animal_name})
            base.update({"birth_date": self.birth_date})
            base.update({"patient_number": self.patient_number})
            base.update({"sterilised": self.sterilised})
            base.update({"animal_sort": self.animal_sort})
            base.update({"diagnosis": self.diagnosis})
            return base

    def to_json(self):
            return json.dumps(self.to_dict())
