import re

from sqladmin.admin_cold_data.utilities.logging import (
    get_error_id,
    raise_exception,
)


def test_get_error_id():
    error_id = get_error_id()
    assert isinstance(error_id, str)
    assert re.match(
        r"^[A-Za-z0-9\-]+-\d{14}-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
        error_id
    )


def test_raise_http_exception():
    class DummyException(Exception):
        pass

    model_name = "TestModel"
    function_name = "test_function"
    args = (1, 2, 3)

    try:
        raise_exception(*args, e=DummyException("Test error"), model_name=model_name, function_name=function_name)
    except Exception as exc:
        from fastapi import HTTPException
        assert isinstance(exc, HTTPException)
        assert exc.status_code == 500
        assert "Error ID" in exc.detail
        assert re.match(
            r"^[A-Za-z0-9\-]+-\d{14}-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
            exc.detail.split("Error ID: ")[1]
        )
