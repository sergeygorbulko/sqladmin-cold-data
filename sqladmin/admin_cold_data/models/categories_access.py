from sqlmodel import SQLModel, Field
from utilities.settings import settings
from sqlalchemy import Column, Integer


class CategoriesAccess(SQLModel, table=True):
    __tablename__ = "CategoriesAccess"
    __table_args__ = {"schema": settings.admin_db_schema}

    group_id: int = Field(
        description="Group ID",
        title="Group ID",
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
        title="Category ID",
        foreign_key=f"{settings.admin_db_schema}.Categories.id",
        primary_key=True,
        sa_column=Column(
            Integer,
            nullable=False,
            comment="Category ID"
        )
    )
