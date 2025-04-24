from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import DiagnosisType
from typing import Optional, List


class DiagnosisTypeRepository(BaseRepository[DiagnosisType]):
    def __init__(self, env):
        super().__init__(env['veterinary_module.diagnosis_type'], "DiagnosisType", self.to_dbo)

    @staticmethod
    def to_dbo(dto: DiagnosisType) -> dict:
        return {
            'id': dto.id,
            'description': dto.description,
            'create_date': dto.create_date,
            'write_date': dto.write_date
        }

    def get_by_name(self, name: str) -> Optional[DiagnosisType]:
        return self.search_one([('sort_name', '=', name)])