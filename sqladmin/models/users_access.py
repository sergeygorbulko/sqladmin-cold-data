from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer
from utilities.settings import settings


class UsersAccess(SQLModel, table=True):
    """
    Admin - Users access to groups
    """
    __tablename__ = "UsersAccess"
    __table_args__ = (
        Field(
            sa_column_kwargs={"schema": settings.admin_db_schema}
        ),
    )
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
    user_id: int = Field(
        description="User ID",
        foreign_key=f"{settings.admin_db_schema}.Users.id",
        primary_key=True,
        sa_column=Column(
            Integer,
            nullable=False,
            comment="User ID"
        )
    )
