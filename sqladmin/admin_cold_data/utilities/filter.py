from sqlalchemy import Column, Integer, Float, Date, DateTime, Boolean, String
from sqlalchemy.sql import Select
from typing import Any, List, Tuple
from datetime import datetime
from sqladmin.admin_cold_data.utilities.settings import settings
from enum import Enum


class FilterOp(str, Enum):
    """
    Filter operations.
    """
    EQ = "eq"
    NE = "ne"
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    IN = "in"
    BETWEEN = "between"
    EMPTY = "empty"
    NOT_EMPTY = "not_empty"
    LIKE = "like"


all_filters_operations = {
    "english": {
        FilterOp.EQ: "equals",
        FilterOp.NE: "not equals",
        FilterOp.GT: "greater than",
        FilterOp.GTE: "greater than or equal",
        FilterOp.LT: "less than",
        FilterOp.LTE: "less than or equal",
        FilterOp.IN: "in",
        FilterOp.BETWEEN: "between",
        FilterOp.EMPTY: "is empty",
        FilterOp.NOT_EMPTY: "is not empty",
        FilterOp.LIKE: "contains",
    },
    "russian": {
        FilterOp.EQ: "равно",
        FilterOp.NE: "не равно",
        FilterOp.GT: "больше чем",
        FilterOp.GTE: "больше или равно",
        FilterOp.LT: "меньше чем",
        FilterOp.LTE: "меньше или равно",
        FilterOp.IN: "в списке",
        FilterOp.BETWEEN: "между",
        FilterOp.EMPTY: "пусто",
        FilterOp.NOT_EMPTY: "не пусто",
        FilterOp.LIKE: "содержит",
    },
}


def get_filter_operations(keys: set[str]) -> List[Tuple[str, str]]:
    """
    Get filter operations based on the provided keys and current UI language.
    Args:
        keys (set[str]): A set of filter operation keys.
    Returns:
        List[Tuple[str, str]]: A list of tuples containing filter operation 
                               key and its corresponding label in the current
                               UI language.
    """
    filters = {
        k: v for k, v in all_filters_operations[
            settings.ui_language
        ].items() if k in keys
    }
    return list(filters.items())


class UniversalFilter:

    def __init__(self, column: Column, title: str = None, parameter_name: str = None):
        self.column = column
        self.title = title or column.name
        self.parameter_name = parameter_name or f"filter_{column.name}"
        self.type = self._detect_type()

    def _detect_type(self) -> str:
        """
        Detect the type of the column.
        Returns:
            str: The type of the column as a string.
        """
        col_type = self.column.type

        if hasattr(col_type, 'impl'):
            col_type = col_type.impl

        visit_name = getattr(col_type, '__visit_name__', None)

        if isinstance(col_type, Integer):
            return "int"
        elif isinstance(col_type, Float):
            return "float"
        elif visit_name in ("numeric", "DECIMAL"):
            return "float"
        elif isinstance(col_type, Boolean):
            return "bool"
        elif isinstance(col_type, (Date, DateTime)):
            return "date"
        elif isinstance(col_type, String):
            return "string"
        elif visit_name in ("VARCHAR", "CHAR", "TEXT", "STRING", "JSON"):
            return "string"

        return "unknown"

    def get_operators(self) -> List[Tuple[str, str]]:
        if self.type == "int" or self.type == "fload":
            return get_filter_operations(
                {FilterOp.EQ, FilterOp.NE, FilterOp.GT, FilterOp.GTE,
                 FilterOp.LT, FilterOp.LTE, FilterOp.IN, FilterOp.BETWEEN,
                 FilterOp.EMPTY, FilterOp.NOT_EMPTY}
            )
