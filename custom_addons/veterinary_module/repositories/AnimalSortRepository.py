from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.models.models import AnimalSort
from typing import Optional, List


class AnimalSortRepository(BaseRepository[AnimalSort]):
    def __init__(self, env) -> None:

        def to_dbo(record:AnimalSort):
            return AnimalSort(
                id=record.id,
                sort_name=record.sort_name,
            )

        super().__init__(env, 'res.animal_sorts', to_dbo)

    def get_by_name(self, name: str) -> Optional[AnimalSort]:
        return self.search_one([('sort_name', '=', name)])