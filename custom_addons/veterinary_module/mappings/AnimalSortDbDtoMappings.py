from typing import List

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.models.models import AnimalSort


def animal_sort_from_db_to_dto(dto: AnimalSort) ->AnimalSortDto:
    return AnimalSortDto(
        id=dto.id,
        sort_name=dto.sort_name
    )

def animal_sort_from_dto_to_db(do: AnimalSortDto) ->object:
    result:object = object()
    result.id = do.id
    result.sort_name = do.sort_name
    return result

def animal_sort_from_dtos_to_dbs(dtos: List[AnimalSortDto]) ->List[object]:
    result = []
    for dto in dtos:
        result.append(animal_sort_from_dto_to_db(dto))
    return result

def animal_sort_from_dbs_to_dtos(dos: List[AnimalSort]) ->List[AnimalSortDto]:
    result = []
    for do in dos:
        result.append(animal_sort_from_db_to_dto(do))
    return result