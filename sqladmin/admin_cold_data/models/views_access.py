from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer
from utilities.settings import settings


class ViewsAccess(SQLModel, table=True):
    """
    Admin - Views access to groups
    """
    __tablename__ = "ViewsAccess"
    __table_args__ = {"schema": settings.admin_db_schema}

    group_id: int = Field(
        description="Group ID",
        foreign_key=f"{settings.admin_db_schema}.AccessGroups.id",
        primary_key=True,
        sa_column=Column(
            Integer,
            nullable=False,
            comment="Group ID"
        ),
    )
    view_id: int = Field(
        description="View ID",
        foreign_key=f"{settings.admin_db_schema}.Views.id",
        primary_key=True,
        sa_column=Column(
            Integer,
            nullable=False,
            comment="View ID"
        ),
    )
