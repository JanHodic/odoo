from custom_addons.veterinary_module.dtos.MedicalDto import MedicalDto
from custom_addons.veterinary_module.services.MedicalService import MedicalService
from odoo import http
from odoo.http import Response, request
import json


class ApiController(http.Controller):
    def __init__(self) -> None:
        self.service: MedicalService = MedicalService(request.env)

    @http.route('/api/medicals', type='http', auth='public', methods=['GET'], csrf=False)
    def get_medicals(self):
        sorts = self.service.list()
        data = [p.to_dict() for p in sorts]
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/medicals/<int:id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_medicals_by_id(self, id:int):
        data = self.service.get_by_id(id)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/medicals/name', type='http', auth='public', methods=['GET'], csrf=False)
    def get_medicals_by_name(self, name:str):
        data = self.service.get_by_name(name)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/medicals', type='json', auth='public', methods=['POST'], csrf=False)
    def create_medical(self, **kwargs):
        dto = MedicalDto.from_dict(kwargs)
        created = self.service.create(dto.to_dict())
        if created:
            return created
        return created.to_dict()

    @http.route('/api/medicals/<int:id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_medical(self, id:int, **kwargs):
        dto = MedicalDto.from_dict(kwargs)
        updated = self.service.update(id, dto.to_dict())
        if updated:
            return updated
        return Response("Not found", status=404)

    @http.route('/api/medicals/<int:id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_medical(self, id:int):
        success = self.service.delete(id)
        return {"deleted": success}
