from typing import List, Optional, TypeVar, Generic, Callable, Any

T = TypeVar('T')  # This will be your DTO type

class BaseRepository(Generic[T]):
    def __init__(self, env, model_name: str, to_dbo: Callable[[Any], T]) -> None:
        """
        :param env: Odoo environment
        :param model_name: The name of the Odoo model (e.g., 'res.partner')
        :param to_dto: A function that takes a record and returns a DTO
        """
        self.env = env
        self.model_name = model_name
        self.to_dbo = to_dbo

    def get_all(self, limit: Optional[int] = None) -> List[T]:
        records = self.env[self.model_name].sudo().search([], limit=limit)
        return [self.to_dbo(record) for record in records]

    def get_by_id(self, id: int) -> Optional[T]:
        record = self.env[self.model_name].sudo().browse(id)
        if not record.exists():
            return None
        return self.to_dbo(record)

    def get_by_domain(self, domain: list) -> List[T]:
        records = self.env[self.model_name].sudo().search(domain)
        return [self.to_dbo(record) for record in records]

    def create(self, values: dict) -> T:
        record = self.env[self.model_name].sudo().create(values)
        return self.to_dbo(record)

    def update(self, id: int, values: dict) -> Optional[T]:
        record = self.env[self.model_name].sudo().browse(id)
        if not record.exists():
            return None
        record.write(values)
        return self.to_dbo(record)

    def delete(self, id: int) -> bool:
        record = self.env[self.model_name].sudo().browse(id)
        if not record.exists():
            return False
        record.unlink()
        return True
