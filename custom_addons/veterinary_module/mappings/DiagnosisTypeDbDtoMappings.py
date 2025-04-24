from typing import List
from custom_addons.veterinary_module.dtos.DiagnosisTypeDto import DiagnosisTypeDto
from custom_addons.veterinary_module.models.models import DiagnosisType


def diagnosis_type_from_db_to_dto(dto: DiagnosisType) ->DiagnosisTypeDto:
    return DiagnosisTypeDto(
        id=dto.id,
        description=dto.description,
        sort_name=dto.sort_name,
        create_date=dto.create_date,
        write_date=dto.write_date,
    )

def diagnosis_type_from_dto_to_db(do: DiagnosisTypeDto) ->object:
    result:object = object()
    result.id = do.id
    result.description = do.description
    result.sort_name = do.sort_name
    result.create_date = do.create_date
    result.write_date = do.write_date
    return result

def diagnosis_type_from_dtos_to_dbs(dtos: List[DiagnosisTypeDto]) ->List[object]:
    result = []
    for dto in dtos:
        result.append(diagnosis_type_from_dto_to_db(dto))
    return result

def diagnosis_type_from_dbs_to_dtos(dos: List[DiagnosisType]) ->List[DiagnosisTypeDto]:
    result = []
    for do in dos:
        result.append(diagnosis_type_from_db_to_dto(do))
    return result