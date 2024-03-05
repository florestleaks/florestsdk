from pydantic import BaseModel


class TorProxyConfig(BaseModel):
    http: str
    https: str
