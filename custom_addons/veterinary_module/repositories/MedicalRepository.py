from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import Medical
from typing import Optional


class MedicalRepository(BaseRepository[Medical]):

    def __init__(self, env):
        super().__init__(env['veterinary_module.medicals'], "Medical", self.to_dbo)

    @staticmethod
    def to_dbo(dto: Medical) -> dict:
        return {
            'id': dto.id,
            'date_time': dto.date_time,
            'description': dto.description,
            'name': dto.name,
            'treatment_ids': dto.treatment_ids,
            'create_date': dto.create_date,
            'write_date': dto.write_date
        }

    def get_by_name(self, name: str) -> Optional[Medical]:
        return self.search_one([('sort_name', '=', name)])