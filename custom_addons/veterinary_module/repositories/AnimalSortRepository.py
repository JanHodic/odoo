from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import AnimalSort
from typing import Optional


class AnimalSortRepository(BaseRepository[AnimalSort]):
    def __init__(self, env):
        super().__init__(env['veterinary_module.animal_sort'], "AnimalSort", self.to_dbo)


    @staticmethod
    def to_dbo(dto: AnimalSort) -> dict:
        return {
            'id': dto.id,
            'sort_name': dto.sort_name,
            'create_date': dto.create_date,
            'write_date': dto.write_date
        }

    def get_by_name(self, name: str) -> Optional[AnimalSort]:
        return self.search_one([('sort_name', '=', name)])