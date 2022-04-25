import os


class ConfigLoader:

    ENV = os.getenv("env", 'dev')

    @classmethod
    def load_config(cls):
        from generic.config.environment_config import DevConfig
        from generic.config.environment_config import TestConfig
        from generic.config.environment_config import StageConfig

        config_by_env = {"dev": DevConfig, "test": TestConfig, "stage": StageConfig}

        return config_by_env[cls.ENV]() #Returns DevConfig, TestConfig or StageConfig

