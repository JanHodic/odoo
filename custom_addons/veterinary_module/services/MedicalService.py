from typing import List, Optional, cast
from custom_addons.veterinary_module.dtos.MedicalDto import MedicalDto
from custom_addons.veterinary_module.mappings.MedicalsDbDtoMappings import medical_from_dbs_to_dtos, \
    medical_from_db_to_dto
from custom_addons.veterinary_module.models.models import Medical, Treatment
from custom_addons.veterinary_module.repositories.MedicalRepository import MedicalRepository
from odoo.api import Environment


class MedicalService:
    def __init__(self, env: Environment) -> None:
        self.repo: MedicalRepository = MedicalRepository(env)

    def list(self) -> List[MedicalDto]:
        return medical_from_dbs_to_dtos(self.repo.get_all())

    def get_by_name(self, name: str) -> Optional[MedicalDto]:
        medical: Medical | None = self.repo.get_by_name(name)
        treatments:[] = []
        if medical:
            for t in medical.treatment_ids:
                treat:Treatment | None = self.repo.get_by_name(t)
                treatments.append(treat)
        return medical_from_db_to_dto(
            medical,
            treatments=treatments
        )

    def get_by_id(self, id: int) -> Optional[MedicalDto]:
        medical: Medical | None = self.repo.get_by_id(id)
        treatments:[] = []
        if medical:
            for t in medical.treatment_ids:
                treat:Treatment | None = self.repo.get_by_name(t)
                treatments.append(treat)

        return medical_from_db_to_dto(
            medical,
            treatments=treatments
        )

    def create(self, medical_dto:dict) -> object:
        return self.repo.create(medical_dto)

    def update(self, id: int, medical_dto:dict) -> Optional[object]:
        return self.repo.update(id, medical_dto)

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)