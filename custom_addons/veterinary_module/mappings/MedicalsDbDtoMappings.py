from typing import List
from custom_addons.veterinary_module.dtos.MedicalDto import MedicalDto
from custom_addons.veterinary_module.models.models import Medical


def medical_from_db_to_dto(dto: Medical) ->MedicalDto:
    return MedicalDto(
        id=dto.id,
        create_date=dto.create_date,
        description=dto.description,
        write_date=dto.write_date,
        date_time=dto.date_time,
        treatments=dto.treatment_ids
    )

def medical_from_dto_to_db(do: MedicalDto) ->object:
    result: object = object()
    result.id = do.id
    result.create_date = do.create_date
    result.description = do.description
    result.write_date = do.write_date
    result.date_time = do.date_time
    result.treatments = []
    return result

def medical_from_dtos_to_dbs(dtos: List[MedicalDto]) ->List[object]:
    result = []
    for dto in dtos:
        result.append(medical_from_dto_to_db(dto))
    return result

def medical_from_dbs_to_dtos(dos: List[Medical]) ->List[MedicalDto]:
    result = []
    for do in dos:
        result.append(medical_from_db_to_dto(do))
    return result