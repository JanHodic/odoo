from odoo import models, fields

class Base(models.AbstractModel):
    _name = 'veterinary_module.base'
    _description = 'Base model with name field'
    _abstract = True
    id:int = fields.Id(string='ID', primary_key=True, required=True)
    create_date = fields.Datetime(readonly=True)
    write_date = fields.Datetime(readonly=True)
