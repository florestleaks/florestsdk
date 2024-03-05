from pydantic import BaseModel


class YaraConfig(BaseModel):
    type_rules: list[str]
