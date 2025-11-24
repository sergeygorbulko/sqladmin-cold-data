from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import Column, String
from models.users import Users
from models.views_ import Views
from models.categories import Categories
from utilities.settings import settings


class AccessGroups(SQLModel, table=True):
    __tablename__ = "AccessGroups"
    __table_args__ = (
        UniqueConstraint(
            "code",
            name="uq_access_groups_code"),
        {"schema": settings.admin_db_schema}
    )

    id: int = Field(primary_key=True)
    code: str = Field(
        description="Access Group Code",
        title="Access Group Code",
        index=True,
        sa_column=Column(
            String(100),
            index=True,
            comment="Access Group Code"
        )
    )
    description: str = Field(
        description="Access Group Description",
        title="Access Group Description",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="Access Group Description"
        )
    )

    users_access: list["Users"] = Relationship(
        back_populates="groups"
    )
    views_access: list["Views"] = Relationship(
        back_populates="groups"
    )
    categories_access: list["Categories"] = Relationship(
        back_populates="groups")
