from custom_addons.veterinary_module.models.models import Treatment
from typing import List, Optional


class AnimalSortRepository:
    def __init__(self, env)->None:
        self.env = env

    def get_all_animal_sorts(self)->List[Treatment]:
        records = self.env['res.animal_sorts'].sudo().search([])
        return [
            Treatment(
                p.id,
                p.sort_name,
                [])
             for p in records]

    def create_animal_sort(self, name: str) -> Treatment:
        order = self.env['res.animal_sorts'].sudo().create({
            'sort_name': name,
        })
        return Treatment(
            order.id,
            order.name,
            []
        )

    def get_animal_sort_by_name(self, name: str) -> Optional[Treatment]:
        record = self.env['res.animal_sorts'].sudo().search({'sort_name': name})
        return Treatment(
            record.id,
            record.name,
            []
        )

    def get_animal_sort_by_id(self, id: int) -> Optional[Treatment]:
        """

        :type id: int
        """
        record = self.env['res.animal_sorts'].sudo().browse(id)
        if not record.exists():
            return None
        return Treatment(
            record.id,
            record.name,
            []
        )

    def update_animal_sort(self, id: int, name: str) -> Optional[Treatment]:
        """

        :param name:
        :type id: int
        """
        record = self.env['res.animal_sorts'].sudo().browse(id)
        if not record.exists():
            return None
        record.name = name
        return Treatment(
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