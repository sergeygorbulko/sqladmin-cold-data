from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import Column, String
from models.users_access import UsersAccess
from utilities.settings import settings


class Users(SQLModel, table=True):
    """
    Admin - Users
    """
    __tablename__ = "Users"
    __table_args__ = (
        UniqueConstraint(
            "user_name",
            name="uq_username"
        ),
        {"schema": settings.admin_db_schema}
    )
    id: int = Field(
        description="User ID",
        primary_key=True,
        sa_column=Column(
            nullable=False,
            comment="User ID"
        )
    )
    user_name: str = Field(
        description="Username",
        index=True,
        sa_column=Column(
            String(100),
            nullable=False,
            comment="Username"
        )
    )
    email: str = Field(
        description="Email",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="Email"
        )
    )

    groups: list["AccessGroups"] = Relationship(
        back_populates="users",
        link_model=UsersAccess
    )
