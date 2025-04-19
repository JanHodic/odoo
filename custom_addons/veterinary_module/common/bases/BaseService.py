from typing import List, Optional, TypeVar

from custom_addons.veterinary_module.common.bases.BaseRepository import BaseRepository
from custom_addons.veterinary_module.common.bases.dtos import BaseDto
from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.mappings.DbDtoMappings import animal_sort_from_db_to_dto, \
    animal_sort_from_dbs_to_dtos
from custom_addons.veterinary_module.repositories.AnimalSortRepository import AnimalSortRepository
from odoo.api import Environment

T = TypeVar('T')  # DBO type
Dto = TypeVar('Dto')  # DTO type

class BaseService:
    def __init__(self, env: Environment) -> None:
        self.repo: BaseRepository = BaseRepository(env, self, )

    def list_get_all(self) -> List[AnimalSortDto]:
        return animal_sort_from_dbs_to_dtos(self.repo.get_all())

    def get_by_id(self, id: int) -> Optional[T]:
        return animal_sort_from_db_to_dto(
            self.repo.get_by_id(id)
        )

    def delete(self, id: int) -> bool:
        return self.repo.delete(id)
    """
        def create(self, dto: BaseDto) -> BaseDto:
            return animal_sort_from_db_to_dto(
                self.repo.create({ "id": 0 ,"sort_name": name })
            )
    
        def update(self, id: int, name: str) -> Optional[AnimalSortDto]:
            return animal_sort_from_db_to_dto(
                self.repo.update({ "id": id, "sort_name": name })
            )
    """
