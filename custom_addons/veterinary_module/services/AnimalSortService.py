from typing import List, Optional

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.mappings.DbDtoMappings import animal_sort_from_db_to_dto, \
    animal_sort_from_dbs_to_dtos
from custom_addons.veterinary_module.repositories.AnimalSortRepository import AnimalSortRepository
from odoo.api import Environment


class AnimalSortService:
    def __init__(self, env: Environment) -> None:
        self.repo: AnimalSortRepository = AnimalSortRepository(env)

    def list_animal_sorts(self) -> List[AnimalSortDto]:
        return animal_sort_from_dbs_to_dtos(self.repo.get_all_animal_sorts(self.repo))

    def get_animal_sort_by_name(self, name: str) -> Optional[AnimalSortDto]:
        return animal_sort_from_db_to_dto(
            self.repo
            .get_animal_sort_by_name(name)
        )

    def get_animal_sort_by_id(self, id: int) -> Optional[AnimalSortDto]:
        return animal_sort_from_db_to_dto(
            self.repo
            .get_animal_sort_by_id(id)
        )

    def create_animal_sort(self, name: str) -> AnimalSortDto:
        return animal_sort_from_db_to_dto(
            self.repo
            .create_animal_sort(name)
        )

    def update_animal_sort(self, id: int, name: str) -> Optional[AnimalSortDto]:
        return animal_sort_from_db_to_dto(
            self.repo
            .update_animal_sort(id, name)
        )

    def delete_animal_sort(self, id: int) -> bool:
        return  self.repo.delete_animal_sort(id)