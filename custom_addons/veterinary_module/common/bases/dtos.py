import json

class BaseDto:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(data: dict) -> "BaseDto":
        return BaseDto(
            id=data.get("id"),
            name=data.get("name")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
