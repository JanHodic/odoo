from custom_addons.veterinary_module.services.TreatmentService import TreatmentService
from odoo import http
from odoo.http import Response, request
import json


class ApiController(http.Controller):
    def __init__(self) -> None:
        self.service: TreatmentService = TreatmentService(request.env)

    @http.route('/api/treatments', type='http', auth='public', methods=['GET'], csrf=False)
    def get_treatments(self):
        sorts = self.service.list()
        data = [p.to_dict() for p in sorts]
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/treatments/<int:id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_treatment_by_id(self, id:int):
        data = self.service.get_by_id(id)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/treatments/name', type='http', auth='public', methods=['GET'], csrf=False)
    def get_treatment_by_name(self, name:str):
        data = self.service.get_by_name(name)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/treatments', type='json', auth='public', methods=['POST'], csrf=False)
    def create_treatment(self):
        data = request.jsonrequest
        name = data.get('name')
        sort = self.service.create(name)
        return sort.to_dict()

    @http.route('/api/treatments/<int:id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_treatment(self, id:int):
        data = request.jsonrequest
        name = data.get('name')
        updated = self.service.update(id, name)
        if updated:
            return updated.to_dict()
        return Response("Not found", status=404)

    @http.route('/api/treatments/<int:id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_treatment(self, id:int):
        success = self.service.delete(id)
        return {"deleted": success}
