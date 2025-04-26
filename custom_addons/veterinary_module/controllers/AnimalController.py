from custom_addons.veterinary_module.dtos.AnimalDto import AnimalDto
from custom_addons.veterinary_module.services.AnimalService import AnimalService
from odoo import http
from odoo.api import Environment
from odoo.http import Response, request
import json


class ApiController(http.Controller):
    def __init__(self) -> None:
        self.service: AnimalService = AnimalService(request.env)

    @http.route('/api/animals', type='http', auth='public', methods=['GET'], csrf=False)
    def get_animals(self):
        sorts = self.service.list()
        data = [p.to_dict() for p in sorts]
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/animals/<int:id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_animal_by_id(self, id:int):
        data = self.service.get_by_id(id)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/animals/name', type='http', auth='public', methods=['GET'], csrf=False)
    def get_animal_by_name(self, name:str):
        data = self.service.get_by_name(name)
        return Response(json.dumps({"data": data}), content_type='application/json')

    @http.route('/api/animals', type='json', auth='public', methods=['POST'], csrf=False)
    def create_animal(self, **kwargs):
        dto = AnimalDto.from_dict(kwargs)
        sort = self.service.create(dto.to_dict())
        return sort

    @http.route('/api/animals/<int:id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_animal(self, id:int, **kwargs):
        dto = AnimalDto.from_dict(kwargs)
        updated = self.service.update(id, dto.to_dict())
        if updated:
            return updated
        return Response("Not found", status=404)

    @http.route('/api/animals/<int:id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_animal(self, id:int):
        success = self.service.delete(id)
        return {"deleted": success}
