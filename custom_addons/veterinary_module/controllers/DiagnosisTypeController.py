from custom_addons.veterinary_module.services.AnimalSortService import AnimalSortService
from custom_addons.veterinary_module.services.DiagnosisService import DiagnosisService
from custom_addons.veterinary_module.services.DiagnosisTypeService import DiagnosisTypeService
from odoo import http
from odoo.api import Environment
from odoo.http import Response, request
import json


class ApiController(http.Controller):
    def __init__(self) -> None:
        self.service: DiagnosisTypeService = DiagnosisTypeService(request.env)

    @http.route('/api/diagnosis_types', type='http', auth='public', methods=['GET'], csrf=False)
    def get_diagnosis_types(self):
        sorts = self.service.list()
        data = [p.to_dict() for p in sorts]
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/diagnosis_types/<int:id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_diagnosis_type_by_id(self, id:int):
        data = self.service.get_by_id(id)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/diagnosis_types/name', type='http', auth='public', methods=['GET'], csrf=False)
    def get_diagnosis_types_by_name(self, name:str):
        data = self.service.get_by_name(name)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/diagnosis_types', type='json', auth='public', methods=['POST'], csrf=False)
    def create_diagnosis_type(self):
        data = request.jsonrequest
        name = data.get('name')
        sort = self.service.create(name)
        return sort.to_dict()

    @http.route('/api/diagnoses/<int:id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_diagnosis_types(self, id:int):
        data = request.jsonrequest
        name = data.get('name')
        updated = self.service.update(id, name)
        if updated:
            return updated.to_dict()
        return Response("Not found", status=404)

    @http.route('/api/diagnosis_types/<int:id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_animal_sort(self, id:int):
        success = self.service.delete(id)
        return {"deleted": success}
