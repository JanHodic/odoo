from typing import List, Optional

from custom_addons.veterinary_module.dtos.TreatmentDto import TreatmentDto
from custom_addons.veterinary_module.mappings.TreatmentDbDtoMappings import treatment_from_db_to_dto, treatment_from_dbs_to_dtos
from custom_addons.veterinary_module.repositories.TreatmentRepository import TreatmentRepository
from odoo.api import Environment


class TreatmentService:
    def __init__(self, env: Environment) -> None:
        self.repo: TreatmentRepository = TreatmentRepository(env)

    def list(self) -> List[TreatmentDto]:
        return treatment_from_dbs_to_dtos(self.repo.get_all())

    def get_by_id(self, id: int) -> Optional[TreatmentDto]:

        return treatment_from_db_to_dto(
            self.repo.get_by_id(id)
        )

    def create(self, treatment_dto:dict) -> object:
        return self.repo.create(treatment_dto)

    def update(self, id: int, treatment_dto:dict) -> Optional[object]:
        return self.repo.update(id, treatment_dto)

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)