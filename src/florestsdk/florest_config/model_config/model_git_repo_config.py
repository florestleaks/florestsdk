from pydantic import BaseModel, HttpUrl


class GitRepoConfig(BaseModel):
    client_crawler_monitoring_url: HttpUrl
    client_crawler_branch: str
    client_yara_rules_url: HttpUrl
    client_yara_rules_branch: str
    client_monitoring_branch: str
    client_monitoring_url: HttpUrl
    user: str
    token: str
