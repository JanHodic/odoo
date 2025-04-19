from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import DiagnosisType
from typing import Optional, List


class DiagnosisTypeRepository(BaseRepository[DiagnosisType]):

    def get_by_name(self, name: str) -> Optional[DiagnosisType]:
        return self.search_one([('sort_name', '=', name)])