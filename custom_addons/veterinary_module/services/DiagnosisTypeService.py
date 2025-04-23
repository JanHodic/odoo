from typing import List, Optional

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.dtos.DiagnosisTypeDto import DiagnosisTypeDto
from custom_addons.veterinary_module.mappings.AnimalSortDbDtoMappings import animal_sort_from_db_to_dto
from custom_addons.veterinary_module.mappings.DiagnosisDbDtoMappings import diagnosis_from_dbs_to_dtos
from custom_addons.veterinary_module.repositories.DiagnosisTypeRepository import DiagnosisTypeRepository
from odoo.api import Environment


class DiagnosisTypeService:
    def __init__(self, env: Environment) -> None:
        self.repo: DiagnosisTypeRepository = DiagnosisTypeRepository(env)

    def list(self) -> list[AnimalSortDto]:
        return diagnosis_from_dbs_to_dtos(self.repo.get_all())

    def get_by_name(self, name: str) -> Optional[DiagnosisTypeDto]:
        return animal_sort_from_db_to_dto(
            self.repo.get_by_name(name),
        )

    def get_by_id(self, id: int) -> Optional[DiagnosisTypeDto]:

        return animal_sort_from_db_to_dto(
            self.repo.get_by_id(id)
        )

    def create(self, name: str) -> DiagnosisTypeDto:
        return animal_sort_from_db_to_dto(
            self.repo.create({ "id": 0 ,"sort_name": name })
        )

    def update(self, id: int, name: str) -> Optional[DiagnosisTypeDto]:
        return animal_sort_from_db_to_dto(
            self.repo.update({ "id": id, "sort_name": name })
        )

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)