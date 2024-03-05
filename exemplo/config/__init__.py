from florestsdk.florest_config import ForestConfiguration

if __name__ == "__main__":
    config_path = "config.toml"
    florest_config = ForestConfiguration(config_path)
    print(florest_config.internal_git_repo_config)
