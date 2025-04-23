from custom_addons.veterinary_module.common.bases.models import Base
from odoo import fields

# Animal sort
class AnimalSort(Base):
    _name = 'veterinary_module.animal_sort'
    _description = 'Animal sort model'
    _inherit = "veterinary_module.base"
    sort_name = fields.Char(max_length=30)

#Type of sickness
class DiagnosisType(Base):
    _name = 'veterinary_module.diagnosis_type'
    _description = 'Diagnosis type model'
    _inherit = "veterinary_module.base"
    sort_name = fields.Char(max_length=30)
    description = fields.Char(max_length=255)

# Treatment
class Treatment(Base):
    _name = 'veterinary_module.treatment'
    _description = 'Treatment model'
    _inherit = "veterinary_module.base"
    date_time = fields.Datetime(fields.Datetime())
    realised = fields.Boolean("False")
    description = fields.Char(max_length=255)
    medical_ids = fields.Many2many(
        "veterinary_module.medical",
        string="Medicals",
        related_name="Medical",
        ondelete="cascade",
        )

# Medical
class Medical(Base):
    _name = 'veterinary_module.medical'
    _description = 'Medical model'
    _inherit = "veterinary_module.base"
    date_time = fields.Datetime(fields.Datetime())
    name = fields.Char(max_length=255)
    description = fields.Char(max_length=255)
    treatment_ids = fields.Many2many(
        "veterinary_module.treatment",
        string="Treatments",
        related_name="Treatment",
        ondelete="cascade",
        )

# Diagnosis
class Diagnosis(Base):
    def __init__(self, env: api.Environment, ids: tuple[IdType, ...], prefetch_ids: Reversible[IdType]):
        super().__init__(env, ids, prefetch_ids)
        self.type = None

    _name = 'veterinary_module.diagnosis'
    _description = 'Diagnosis model'
    _inherit = "veterinary_module.base"
    date_time = fields.Datetime(fields.Datetime())
    cured = fields.Boolean("False")
    description = fields.Char(max_length=255)
    type_id = fields.Many2one(
        "veterinary_module.diagnosis_type",
        string="DiagnosisType",
        related_name="diagnosis_type",
        ondelete="cascade"
    )
    treatment_ids = fields.Many2one(
        "veterinary_module.treatment",
        string="Treatments",
        ondelete="cascade",
        related_name="treatment",
        )

# Animal
class Animal(Base):
    _name = 'veterinary_module.animal'
    _description = 'Animal model'
    _inherit = "veterinary_module.base"
    animal_name = fields.Char(max_length=255)
    birth_date = fields.Datetime(fields.Datetime())
    patient_number = fields.Char(max_length=255)
    sterilised = fields.Boolean()
    animal_sort_id = fields.Many2one(
        "veterinary_module.animal_sort",
        string="AnimalSort",
        related_name="animal_sort",
        ondelete="cascade",
        unique=True)
    diagnosis_ids = fields.Many2many(
        "veterinary_module.diagnoses",
        string="Diagnoses",
        related_name="diagnoses",
        ondelete="cascade"
    )