class TreatmentDto(BaseDto):
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

    def __init__(self, id: int, cured: bool, type: DiagnosisTypeDto, description: str, treatments: List[TreatmentDto],
                 create_date:Datetime, write_date:Datetime) -> None:
        super().__init__(id, create_date, write_date)
        self.cured: bool = cured
        self.type:DiagnosisTypeDto = type
        self.description:str = description
        self.treatments:List[TreatmentDto] = treatments

    def to_dict(self) -> Dict[str, str | int | Datetime]:
        base = super().to_dict()
        base.update({"cured": self.cured})
        base.update({"type": self.type})
        base.update({"description": self.description})
        base.update({"treatments": self.treatments})
        return base

    @staticmethod
    def from_dict(data: dict) -> "DiagnosisDto":
        return DiagnosisDto(
            id=data.get("id"),
            create_date=data.get("create_date"),
            write_date=data.get("write_date"),
            cured=data.get("cured"),
            type=data.get("type"),
            description=data.get("description"),
            treatments=data.get("treatments"),
        )

    def to_json(self):
        return json.dumps(self.to_dict())