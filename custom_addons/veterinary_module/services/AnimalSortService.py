from typing import List, Optional

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.repositories import AnimalSortRepository
from odoo.api import Environment


class AnimalSortService:
    def __init__(self, env: Environment) -> None:
        self.repo: AnimalSortRepository = AnimalSortRepository(env)

    def list_animal_sorts(self) -> List[AnimalSortDto]:
        return self.repo.get_all_animal_sorts()

    def get_animal_sort_by_name(self, name: str) -> [AnimalSortDto]:
        return self.repo.get_animal_sort_by_name(name)

    def get_animal_sort(self, id: int) -> bool:
        return self.repo.get_animal_sort_by_id(id)

    def create_animal_sort(self, name: str) -> AnimalSortDto:
        return self.repo.AnimalSortRepository.create_animal_sort (name)

    def update_animal_sort(self, id: int, name: str) -> Optional[AnimalSortDto]:
        return self.repo.AnimalSortRepository.update_animal_sort(id, name)

    def delete_animal_sort(self, id: int) -> bool:
        return self.repo.AnimalSortRepository.delete_animal_sort(id)