from sqlmodel import SQLModel, Field
from utilities.settings import settings
from sqlalchemy import Column, Integer


class CategoriesAccess(SQLModel, table=True):
    __tablename__ = "CategoriesAccess"
    __table_args__ = {"schema": settings.db_schema}

    group_id: int = Field(
        description="Group ID",
        foreign_key=f"{settings.admin_db_schema}.AccessGroups.id",
        primary_key=True,
        sa_column=Column(
            Integer,
            nullable=False,
            comment="Group ID"
        )
    )
    category_id: int = Field(
        description="Category ID",
        foreign_key=f"{settings.admin_db_schema}.Categories.id",
        primary_key=True,
        sa_column=Column(
            Integer,
            nullable=False,
            comment="Category ID"
        )
    )
