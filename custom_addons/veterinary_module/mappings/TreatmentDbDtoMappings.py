from typing import List, Tuple

from custom_addons.veterinary_module.dtos.MedicalDto import MedicalDto
from custom_addons.veterinary_module.dtos.TreatmentDto import TreatmentDto
from custom_addons.veterinary_module.models.models import AnimalSort, Treatment


def treatment_from_db_to_dto(dto: Treatment, medicals:[]) ->TreatmentDto:
    return TreatmentDto(
        id=dto.id,
        create_date=dto.create_date,
        write_date=dto.write_date,
        realised=dto.realised,
        date_time=dto.date_time,
        description=dto.description,
        medicals=medicals,
    )

def treatment_from_dto_to_db(do: TreatmentDto) ->object:
    result:object = object()
    result.id = do.id
    result.medicals = []
    result.realised = do.realised
    result.date_time = do.date_time
    result.description = do.description
    return result

def treatment_from_dtos_to_dbs(dtos: List[TreatmentDto]) ->List[object]:
    result = []
    for dto in dtos:
        result.append(treatment_from_dto_to_db(dto))
    return result

def treatment_from_dbs_to_dtos(dos: List[Treatment]) ->List[TreatmentDto]:
    result = []

    for do in dos:
        result.append(treatment_from_db_to_dto(do))
    return result