from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import Animal
from typing import Optional


class AnimalRepository(BaseRepository[Animal]):

    def __init__(self, env):
        super().__init__(env['veterinary_module.animals'], "Animal", self.to_dbo)

    @staticmethod
    def to_dbo(dto: Animal) -> dict:
        return {
            'id': dto.id,
            'animal_name': dto.animal_name,
            'animal_sort_id': dto.animal_sort_id,
            'birth_date': dto.birth_date,
            'patient_number': dto.patient_number,
            'diagnosis_ids': dto.diagnosis_ids,
            'sterilised': dto.sterilised,
            'create_date': dto.create_date,
            'write_date': dto.write_date
        }

    def get_by_name(self, name: str) -> Optional[Animal]:
        return self.search_one([('animal_name', '=', name)])