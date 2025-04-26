from typing import List

from custom_addons.veterinary_module.dtos.AnimalDto import AnimalDto
from custom_addons.veterinary_module.models.models import Animal, Diagnosis

def animal_from_db_to_dto(dto: Animal, diagnoses:[], animal_sort_name:str) ->AnimalDto:
    return AnimalDto(
        id=dto.id,
        animal_name=dto.animal_name,
        patient_number=dto.patient_number,
        write_date=dto.write_date,
        create_date=dto.create_date,
        birth_date=dto.birth_date,
        sterilised=dto.sterilised,
        animal_sort=animal_sort_name,
        diagnoses=diagnoses
    )

def animal_from_dto_to_db(do: AnimalDto, animal_sort_id:int, diagnoses:[]) ->object:
    result:object = object()
    result.animal_name = do.animal_name
    result.patient_number = do.patient_number
    result.write_date = do.write_date
    result.create_date = do.create_date
    result.birth_date = do.birth_date
    result.sterilised = do.sterilised
    result.animal_sort_id = animal_sort_id,
    result.diagnoses = diagnoses
    return result

def animal_from_dtos_to_dbs(dtos: List[AnimalDto]) ->List[object]:
    result = []
    for dto in dtos:
        result.append(animal_from_dto_to_db(dto, 0, []))
    return result

def animal_from_dbs_to_dtos(dos: List[Animal]) ->List[AnimalDto]:
    result = []
    for do in dos:
        result.append(animal_from_db_to_dto(do))
    return result