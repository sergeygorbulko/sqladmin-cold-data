from pydantic_settings import BaseSettings
from pydantic import ConfigDict, SecretStr
from typing import List


class Settings(BaseSettings):
    model_config = ConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8"
    )

    # Application settings
    logging_conf: str = "logging.conf"
    env_name: str = "dev"
    system_name: str = "sqladmin-cold-data"
    link_root: str = "http://localhost:8080/admin"
    version: str = "0.1.0"
    bind_host: str = "0.0.0.0"
    dind_port: int = 8080
    gracefull_time_out: int = 30
    ui_language: str = "english"  # english, russian

    # admin database
    admin_db_url_async: str = "sqlite+aiosqlite:///./sqladmin.db"
    admin_db_pool_size: int = 10
    admin_db_max_overflow: int = 30
    admin_db_echo: bool = False
    admin_db_schema: str = "main"


settings = Settings()
