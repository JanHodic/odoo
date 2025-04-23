from typing import List

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.models.models import AnimalSort


def diagnosis_from_db_to_dto(dto: AnimalSort) ->AnimalSortDto:
    return AnimalSortDto(
        id=dto.id,
        sort_name=dto.sort_name
    )

def diagnosis_from_dto_to_db(do: AnimalSortDto) ->AnimalSort:
    return AnimalSort(
        do.id,
        do.sort_name
    )

def diagnosis_from_dtos_to_dbs(dtos: List[AnimalSortDto]) ->List[AnimalSort]:
    list = []
    for dto in dtos:
        list.append(diagnosis_from_dto_to_db(dto))
    return list

def diagnosis_from_dbs_to_dtos(dos: List[AnimalSort]) ->List[AnimalSortDto]:
    list = []
    for do in dos:
        list.append(diagnosis_from_db_to_dto(do))
    return list