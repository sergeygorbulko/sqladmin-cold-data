from sqladmin import settings


async def test_import():
    assert settings is not None
