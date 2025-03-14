import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class CommonSettings:
    DB_PASSWORD: str
    DB_USER: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int

    def __init__(self):
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_PORT = int(os.getenv("DB_PORT", 5432))


class Settings(CommonSettings):
    APP_NAME: str = "Mura test"

    TEST_DB_NAME: str = "test_db"

    CHATGPT_API_KEY: str = os.getenv("CHATGPT_API_KEY")
    CHATGPT_API_URL: str = os.getenv("CHATGPT_API_URL", "https://api.openai.com/v1/")
    CHATGPT_MODEL: str = os.getenv("CHATGPT_MODEL", "davinci")

    def __init__(self):
        super().__init__()
        self.APP_NAME = os.getenv("APP_NAME", "Mura test")
        self.TEST_DB_NAME = os.getenv("TEST_DB_NAME", "test_db")

    def copy(self, settings: "Settings"):
        settings_to_copy = vars(settings)
        for setting_key in settings_to_copy.keys():
            default_value = settings_to_copy[setting_key]
            setattr(self, setting_key, default_value)


@lru_cache
def get_settings():
    return Settings()


settings: Settings = get_settings()
