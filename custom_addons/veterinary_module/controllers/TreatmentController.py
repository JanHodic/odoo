from custom_addons.veterinary_module.dtos.TreatmentDto import TreatmentDto
from custom_addons.veterinary_module.services.TreatmentService import TreatmentService
import odoo
from odoo.http import Response, request
import json


class ApiController(odoo.http.Controller):
    def __init__(self) -> None:
        self.service: TreatmentService = TreatmentService(request.env)

    @odoo.http.route('/api/treatments', type='http', auth='public', methods=['GET'], csrf=False)
    def get_treatments(self):
        sorts = self.service.list()
        data = [p.to_dict() for p in sorts]
        return Response(json.dumps({"data": data}), content_type='application/json')

    @odoo.http.route('/api/treatments/<int:id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_treatment_by_id(self, id:int):
        data = self.service.get_by_id(id)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @odoo.http.route('/api/treatments', type='json', auth='public', methods=['POST'], csrf=False)
    def create_treatment(self, **kwargs):
        dto = TreatmentDto.from_dict(kwargs)
        sort = self.service.create(dto.to_dict())
        return sort

    @odoo.http.route('/api/treatments/<int:id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_treatment(self, id:int, **kwargs):
        dto = TreatmentDto.from_dict(kwargs)
        updated = self.service.update(id, dto.to_dict())
        if updated:
            return updated
        return Response("Not found", status=404)

    @odoo.http.route('/api/treatments/<int:id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_treatment(self, id:int):
        success = self.service.delete(id)
        return {"deleted": success}
