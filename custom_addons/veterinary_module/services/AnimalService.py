from typing import List, Optional

from custom_addons.veterinary_module.dtos.AnimalDto import AnimalDto
from custom_addons.veterinary_module.mappings.AnimalDbDtoMappings import animal_from_dbs_to_dtos, animal_from_db_to_dto
from custom_addons.veterinary_module.models.models import Animal, Diagnosis
from custom_addons.veterinary_module.repositories.AnimalRepository import AnimalRepository
from custom_addons.veterinary_module.repositories.AnimalSortRepository import AnimalSortRepository
from custom_addons.veterinary_module.repositories.DiagnosisRepository import DiagnosisRepository
from odoo.api import Environment


class AnimalService:
    def __init__(self, env: Environment) -> None:
        self.repo: AnimalRepository = AnimalRepository(env)
        self.diagRepo: DiagnosisRepository = DiagnosisRepository(env)
        self.sortRepo: AnimalSortRepository = AnimalSortRepository(env)

    def list(self) -> List[AnimalDto]:
        return animal_from_dbs_to_dtos(self.repo.get_all())

    def get_by_name(self, name: str) -> Optional[AnimalDto]:
        animal: Animal | None = self.repo.get_by_name(name)
        diagnoses: [] = []
        animal_sort_name: str = self.sortRepo.get_by_id(animal.animal_sort_id).sort_name
        if animal:
            for d in animal.diagnosis_ids:
                diagnoses.append(self.diagRepo.get_by_id(d))
        return animal_from_db_to_dto(
            animal,
            diagnoses=diagnoses,
            animal_sort_name=animal_sort_name
        )

    def get_by_id(self, id: int) -> Optional[AnimalDto]:

        animal:Animal =self.repo.get_by_id(id)
        diagnoses:List[Diagnosis] =[]
        animal_sort_name: str = self.sortRepo.get_by_id(animal.animal_sort_id).sort_name
        for d in animal.diagnosis_ids:
            diag:Diagnosis| None = self.diagRepo.get_by_id(d)
            if diag: diagnoses.append(diag)

        return animal_from_db_to_dto(
            animal,
            diagnoses=diagnoses,
            animal_sort_name=animal_sort_name
        )

    def create(self, animal_dto:dict) -> object:
        return self.repo.create(animal_dto)

    def update(self, id: int, animal_dto:dict) -> Optional[object]:
        return self.repo.update(id, animal_dto)

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)