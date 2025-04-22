from typing import List, Optional

from custom_addons.veterinary_module.dtos.DiagnosisDto import DiagnosisDto
from custom_addons.veterinary_module.mappings.DbDtoMappings import animal_sort_from_db_to_dto, \
    animal_sort_from_dbs_to_dtos
from custom_addons.veterinary_module.repositories.DiagnosisRepository import DiagnosisRepository
from odoo.api import Environment


class DiagnosisService:
    def __init__(self, env: Environment) -> None:
        self.repo: DiagnosisRepository = DiagnosisRepository(env)

    def list(self) -> List[DiagnosisDto]:
        return animal_sort_from_dbs_to_dtos(self.repo.get_all())

    def get_by_name(self, name: str) -> Optional[DiagnosisDto]:
        return animal_sort_from_db_to_dto(
            self.repo.get_by_name(name),
        )

    def get_by_id(self, id: int) -> Optional[DiagnosisDto]:

        return animal_sort_from_db_to_dto(
            self.repo.get_by_id(id)
        )

    def create(self, name: str) -> DiagnosisDto:
        return animal_sort_from_db_to_dto(
            self.repo.create({ "id": 0 ,"sort_name": name })
        )

    def update(self, id: int, name: str) -> Optional[DiagnosisDto]:
        return animal_sort_from_db_to_dto(
            self.repo.update({ "id": id, "sort_name": name })
        )

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)