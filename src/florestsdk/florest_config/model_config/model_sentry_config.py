from pydantic import BaseModel


class SentryConfig(BaseModel):
    dsn: str
    traces_sample_rate: int
    profiles_sample_rate: int
    enable_tracing: bool
