from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import Treatment
from typing import Optional


class TreatmentRepository(BaseRepository[Treatment]):

    def __init__(self, env):
        super().__init__(env['veterinary_module.treatments'], "Treatment", self.to_dbo)

    @staticmethod
    def to_dbo(dto: Treatment) -> dict:
        return {
            'id': dto.id,
            'description': dto.description,
            'date_time': dto.date_time,
            'medical_ids': dto.medical_ids,
            'realised': dto.realised,
            'create_date': dto.create_date,
            'write_date': dto.write_date
        }