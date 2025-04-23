from typing import List

from custom_addons.veterinary_module.dtos.AnimalDto import AnimalDto
from custom_addons.veterinary_module.dtos.DiagnosisDto import DiagnosisDto

from custom_addons.veterinary_module.models.models import Animal, Diagnosis


def animal_sort_from_db_to_dto(dto: Animal, diagnosis:DiagnosisDto) ->AnimalDto:
    return AnimalDto(
        id=dto.id,
        animal_name=dto.animal_name,
        patient_number=dto.patient_number,
        write_date=dto.write_date,
        create_date=dto.create_date,
        birth_date=dto.birth_date,
        sterilised=dto.sterilised,
        animal_sort=dto.animal_sort_id,
        diagnosis=diagnosis.type.sort_name
    )

def animal_sort_from_dto_to_db(do: AnimalDto, diagnosis_name:int) ->object:
    result:object = object()
    result.animal_name = do.animal_name
    result.patient_number = do.patient_number
    result.write_date = do.write_date
    result.create_date = do.create_date
    result.birth_date = do.birth_date
    result.sterilised = do.sterilised
    result.animal_sort_id = do.animal_sort
    result.diagnosis = diagnosis_name
    return result

def animal_sort_from_dtos_to_dbs(dtos: List[AnimalDto]) ->List[object]:
    list = []
    for dto in dtos:
        list.append(animal_sort_from_dto_to_db(dto))
    return list

def animal_sort_from_dbs_to_dtos(dos: List[Animal]) ->List[AnimalDto]:
    list = []
    for do in dos:
        list.append(animal_sort_from_db_to_dto(do))
    return list