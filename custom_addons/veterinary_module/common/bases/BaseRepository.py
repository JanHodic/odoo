from typing import List, Optional, TypeVar, Generic, Callable, Any

T = TypeVar('T')  # DBO type


class BaseRepository(Generic[T]):
    def __init__(self, env, model_name: str, to_dbo: Callable[[Any], T]) -> None:
        """
        :param env: Odoo environment
        :param model_name: Odoo model name (e.g. 'res.partner')
        :param to_dbo: Function to map a record to a DBO
        """
        self.env = env
        self.model_name = model_name
        self.to_dbo = to_dbo

    def get_all(self, limit: Optional[int] = None, offset: int = 0) -> List[T]:
        records = self.env[self.model_name].sudo().search([], limit=limit, offset=offset)
        return [self.to_dbo(record) for record in records]

    def get_by_id(self, id: int) -> Optional[T]:
        record = self.env[self.model_name].sudo().browse(id)
        return self.to_dbo(record) if record.exists() else None

    def get_by_ids(self, ids: List[int]) -> List[T]:
        records = self.env[self.model_name].sudo().browse(ids)
        return [self.to_dbo(r) for r in records if r.exists()]

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

    def search(self, domain: list, limit: Optional[int] = None, offset: int = 0, order: Optional[str] = None) -> List[T]:
        records = self.env[self.model_name].sudo().search(domain, limit=limit, offset=offset, order=order)
        return [self.to_dbo(r) for r in records]

    def search_one(self, domain: list) -> Optional[T]:
        record = self.env[self.model_name].sudo().search(domain, limit=1)
        return self.to_dbo(record) if record else None

    def search_ids(self, domain: list) -> List[int]:
        return self.env[self.model_name].sudo().search(domain).ids

    def search_read(self, domain: list, fields: list = None, limit: Optional[int] = None, offset: int = 0, order: Optional[str] = None) -> List[dict]:
        return self.env[self.model_name].sudo().search_read(domain, fields=fields, limit=limit, offset=offset, order=order)

    def search_count(self, domain: list) -> int:
        return self.env[self.model_name].sudo().search_count(domain)

    def exists(self, id: int) -> bool:
        record = self.env[self.model_name].sudo().browse(id)
        return record.exists()
