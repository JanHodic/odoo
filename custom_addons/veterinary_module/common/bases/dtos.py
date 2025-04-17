import json

class BaseDto:
    def __init__(self, id: int):
        self.id = id

    @staticmethod
    def from_dict(data: dict) -> "BaseDto":
        return BaseDto(
            id=data.get("id"),
        )

    def to_dict(self):
        return {
            "id": self.id,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
