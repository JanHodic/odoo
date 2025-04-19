from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import Diagnosis, AnimalSort
from typing import Optional


class DiagnosisRepository(BaseRepository[Diagnosis]):

    def __init__(self, env):
        super().__init__(env['veterinary_module.diagnoses'], "Diagnosis", self.to_dbo)

    @staticmethod
    def to_dbo(dto: Diagnosis) -> dict:
        return {
            'id': dto.id,
            'date_time': dto.date_time,
            'description': dto.description,
            'cured': dto.cured,
            'treatment_ids': dto.treatment_ids,
            'type_id': dto.type_id,
            'create_date': dto.create_date,
            'write_date': dto.write_date
        }