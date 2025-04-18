import json

from odoo.fields import Datetime


class BaseDto:
    def __init__(self, id: int, create_date:Datetime=None, write_date:Datetime=None) -> None:
        self.id = id
        self.create_date = create_date
        self.write_date = write_date

    @staticmethod
    def from_dict(data: dict) -> "BaseDto":
        return BaseDto(
            id=data.get("id"),
            create_date=data.get("create_date"),
            write_date=data.get("write_date"),
        )

    def to_dict(self):
        result = {"id": self.id,}
        if self.create_date: result.update({"create_date": self.create_date})
        if self.create_date: result.update({"write_date": self.write_date})
        return result

    def to_json(self):
        return json.dumps(self.to_dict())
