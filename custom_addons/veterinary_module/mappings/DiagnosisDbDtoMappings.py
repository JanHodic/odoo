from typing import List

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.dtos.DiagnosisDto import DiagnosisDto
from custom_addons.veterinary_module.models.models import Diagnosis


def diagnosis_from_db_to_dto(dto: Diagnosis) ->DiagnosisDto:
    return DiagnosisDto(
        id=dto.id,
        create_date=dto.create_date,
        write_date=dto.write_date,
        cured=dto.cured,
        type=dto.type,
        description=dto.description,
        treatments=dto.treatment_ids,
    )

def diagnosis_from_dto_to_db(do: DiagnosisDto) ->object:
    result:object = object()
    result.id = do.id
    result.create_date = do.create_date
    result.write_date = do.write_date
    result.cured = do.cured
    result.type = do.type
    result.description = do.description
    result.treatments = []
    return result

def diagnosis_from_dtos_to_dbs(dtos: List[DiagnosisDto]) ->List[object]:
    result = []
    for dto in dtos:
        result.append(diagnosis_from_dto_to_db(dto))
    return result

def diagnosis_from_dbs_to_dtos(dos: List[Diagnosis]) ->List[DiagnosisDto]:
    result = []
    for do in dos:
        result.append(diagnosis_from_db_to_dto(do))
    return result