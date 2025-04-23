from typing import List, Tuple

from custom_addons.veterinary_module.dtos.AnimalSortDto import AnimalSortDto
from custom_addons.veterinary_module.dtos.MedicalDto import MedicalDto
from custom_addons.veterinary_module.dtos.TreatmentDto import TreatmentDto
from custom_addons.veterinary_module.models.models import AnimalSort, Treatment


def treatment_from_db_to_dto(dto: Treatment) ->TreatmentDto:
    return TreatmentDto(
        id=dto.id,
        create_date=dto.create_date,
        write_date=dto.write_date,
        realised=dto.realised,
        date_time=dto.date_time,
        description=dto.description,
        medicals=dto.medical_ids,
    )

def treatment_from_dto_to_db(do: TreatmentDto) ->object:
    result:object = object()
    result.id = do.id
    result.medicals = do.medicals

    return result

def treatment_from_dtos_to_dbs(dtos: List[TreatmentDto]) ->List[MedicalDto]:
    result = []
    for dto in dtos:
        list.append(treatment_from_dto_to_db(dto))
    return result

def treatment_from_dbs_to_dtos(dos: List[Treatment], medicals_dto:List[Tuple[MedicalDto, str]]) ->List[TreatmentDto]:
    result = []

    for do in dos:
        filtered_medicals = [dto for dto, tag in medicals_dto if tag in do.medical_ids]
        result.append(treatment_from_db_to_dto(do))
    return result