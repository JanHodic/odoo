import uuid

from custom_addons.veterinary_module.models.models import AnimalSort
from typing import List, Optional


class AnimalSortRepository:
    def __init__(self, env)->None:
        self.env = env

    def get_all_animal_sorts(self)->List[AnimalSort]:
        records = self.env['res.animal_sorts'].sudo().search([])
        return [
            AnimalSort(
                p.id,
                p.sort_name,
                [])
             for p in records]

    def create_animal_sort(self, name: str) -> AnimalSort:
        order = self.env['res.animal_sorts'].sudo().create({
            'sort_name': name,
        })
        return AnimalSort(
            order.id,
            order.name,
            []
        )

    def get_animal_sort_by_name(self, name: str) -> Optional[AnimalSort]:
        record = self.env['res.animal_sorts'].sudo().search({'sort_name': name})
        return AnimalSort(
            record.id,
            record.name,
            []
        )

    def get_animal_sort_by_id(self, id: int) -> Optional[AnimalSort]:
        """

        :type id: int
        """
        record = self.env['res.animal_sorts'].sudo().browse(id)
        if not record.exists():
            return None
        return AnimalSort(
            record.id,
            record.name,
            []
        )

    def update_animal_sort(self, id: int, name: str) -> Optional[AnimalSort]:
        """

        :param name:
        :type id: int
        """
        record = self.env['res.animal_sorts'].sudo().browse(id)
        if not record.exists():
            return None
        record.name = name
        return AnimalSort(
            record.id,
            record.name,
            []
        )

    def delete_animal_sort(self, id: int) -> bool:
        record = self.env['res.animal_sorts'].sudo().browse(id)
        if not record.exists():
            return False
        record.unlink()
        return True