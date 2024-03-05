from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    server: str
    ports: list[int]
    connection_max: int
    enabled: bool
