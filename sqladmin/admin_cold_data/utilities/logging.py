import os
import logging
import logging.config
import yaml
import json
import socket
import uuid
import re

from datetime import datetime, timezone
from sqladmin.admin_cold_data.utilities.settings import settings
from fastapi import HTTPException
from typing import NoReturn

log = logging.getLogger(__name__)


def get_error_id() -> str:
    """Generate a unique error ID using hostname, timestamp, and UUID."""
    hostname = socket.gethostname()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())
    return f"{hostname}-{timestamp}-{unique_id}"


def raise_exception(
        *args,
        e: Exception,
        model_name: str,
        function_name: str
) -> NoReturn:
    """Raise an HTTPException with a unique error ID and log the error."""
    error_id = get_error_id()
    log.exception(
        "Error ID: %s | Model: %s | Function: %s | Args: %s",
        error_id,
        model_name,
        function_name,
        args,
        exc_info=e
    )
    raise HTTPException(
        status_code=500,
        detail=f"An internal server error occurred. Please contact support with Error ID: {error_id}"
    )

def setup_logging(logging_config_file: str = "logging.yaml") -> None:
    """Set up logging configuration from a YAML file."""
    try:
        if os.path.exists(logging_config_file):
            with open(logging_config_file, 'r') as f:
                config = yaml.safe_load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=logging.INFO)
            log.warning("Logging configuration file not found. Using basic configuration.")
    except Exception as e:
        log.exception("Failed to set up logging configuration.", exc_info=e)



class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for logging."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "filename": record.filename,
            "line": record.lineno,
            "function": record.funcName,
        }
        if record.name:
            log_entry["logger"] = record.name
        if record.pathname:
            log_entry["pathname"] = record.pathname
        if record.lineno:
            log_entry["lineno"] = record.lineno
        if record.funcName:
            log_entry["funcName"] = record.funcName
        if record.exc_info:
            log_entry["exec_info"] = self.formatException(record.exc_info)

        for key, value in record.__dict__.items():
            if key not in logging.LogRecord("", 0, "", 0, "", (), None).__dict__:
                log_entry[key] = value
        
        level = log_entry["level"].lower()

        valid_levels = {
            "ERROR", "DEBUG", "INFO", "WARNING", "CRITICAL", "FATAL", "TRACE"
        }
        log_entry["level"] = level if level in valid_levels else "INFO"

        return json.dumps(log_entry, ensure_ascii=False, default=str)
