from typing import Optional

from custom_addons.veterinary_module.dtos.DiagnosisTypeDto import DiagnosisTypeDto
from custom_addons.veterinary_module.mappings.DiagnosisTypeDbDtoMappings import diagnosis_type_from_dbs_to_dtos, \
    diagnosis_type_from_db_to_dto
from custom_addons.veterinary_module.repositories.DiagnosisTypeRepository import DiagnosisTypeRepository
from odoo.api import Environment

class DiagnosisTypeService:
    def __init__(self, env: Environment) -> None:
        self.repo: DiagnosisTypeRepository = DiagnosisTypeRepository(env)

    def list(self) -> list[DiagnosisTypeDto]:
        return diagnosis_type_from_dbs_to_dtos(self.repo.get_all())

    def get_by_name(self, name: str) -> Optional[DiagnosisTypeDto]:
        return diagnosis_type_from_db_to_dto(
            self.repo.get_by_name(name),
        )

    def get_by_id(self, id: int) -> Optional[DiagnosisTypeDto]:

        return diagnosis_type_from_db_to_dto((
            self.repo.get_by_id(id)
        ))

    def create(self, diag_type: DiagnosisTypeDto) -> DiagnosisTypeDto:
        return diagnosis_type_from_db_to_dto(
            self.repo.create({
                "id": 0 ,
                "sort_name": diag_type.sort_name,
                "description": diag_type.description
            })
        )

    def update(self, diag_type: DiagnosisTypeDto) -> Optional[DiagnosisTypeDto]:
        return diagnosis_type_from_db_to_dto(
            self.repo.update(
                diag_type.id,
                {
                    "id": diag_type.id,
                    "sort_name": diag_type.sort_name,
                    "description": diag_type.description
                })
        )

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)