from sqladmin import settings


def test_import():
    """
    Test import settings
    """
    assert settings is not None


def test_app_settings():
    """
    Test app settings
    """
    assert settings.logging_conf == "logging.conf"
    assert settings.ui_language in {"english", "russian"}
    assert settings.env_name in {"dev", "prod", "test"} 
    assert settings.system_name == "sqladmin-cold-data"
    assert settings.version == "0.1.0" 
    assert settings.link_root == "http://localhost:8080/admin"
    assert settings.bind_host == "0.0.0.0"
    assert settings.dind_port == 8080
    assert settings.gracefull_time_out == 30


def test_admin_db_settings():
    """
    Test admin database settings
    """
    assert settings.admin_db_url_async == "sqlite+aiosqlite:///./sqladmin.db"
    assert settings.admin_db_pool_size == 10
    assert settings.admin_db_max_overflow == 30
    assert settings.admin_db_echo is False
    assert settings.admin_db_schema == "main"
