from sqladmin import settings


async def test_import():
    """
    Test import settings
    """
    assert settings is not None


async def test_app_settings():
    """
    Test app settings
    """
    assert settings.admin_db_schema == "admin_cold_data"
    assert settings.ui_language in {"english", "russian"}
    assert settings.page_size > 0
    assert settings.max_page_size >= settings.page_size
    assert settings.database_url.startswith("postgresql+asyncpg://")
