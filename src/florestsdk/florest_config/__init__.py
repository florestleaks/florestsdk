from pathlib import Path

import toml

from florestsdk import ROOT_DIR
from florestsdk.florest_config.model_config.model_database_config import DatabaseConfig
from florestsdk.florest_config.model_config.model_git_repo_config import GitRepoConfig
from florestsdk.florest_config.model_config.model_network_proxy_tor import TorProxyConfig
from florestsdk.florest_config.model_config.model_notification_config import NotificationSender
from florestsdk.florest_config.model_config.model_sentry_config import SentryConfig
from florestsdk.florest_config.model_config.model_yara_config import YaraConfig


class ForestConfiguration:
    def __init__(self, config_file=ROOT_DIR):
        self.internal_database_connection_config = DatabaseConfig
        self.internal_sentry = SentryConfig
        self.internal_notification_sender_config = NotificationSender
        self.internal_tor_proxy_config = TorProxyConfig
        self.internal_git_repo_config = GitRepoConfig
        self.internal_yara_support_rules_config = YaraConfig
        self.config_file = Path(config_file)  # Convertendo para um objeto Path
        self.load_config()

    def load_config(self):
        with self.config_file.open("r") as file:  # Usando o método open de um objeto Path
            config_data = toml.load(file)
            self.internal_database_connection_config = DatabaseConfig(
                **config_data.get("Internal_Database_Connection_Config", {})
            )
            self.internal_sentry = SentryConfig(**config_data.get("Internal_Sentry", {}))
            self.internal_notification_sender_config = NotificationSender(
                **config_data.get("Notification_Sender", {})
            )
            self.internal_tor_proxy_config = TorProxyConfig(
                **config_data.get("Internal_Network_Proxy", {})
            )
            self.internal_git_repo_config = GitRepoConfig(**config_data.get("Internal_GitRepo", {}))
            self.internal_yara_support_rules_config = YaraConfig(
                **config_data.get("Internal_Yara", {})
            )
