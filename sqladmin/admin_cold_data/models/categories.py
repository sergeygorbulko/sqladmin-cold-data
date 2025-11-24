from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import Column, String
from models.categories_access import CategoriesAccess
from utilities.settings import settings


class Categories(SQLModel, table=True):
    """
    Admin - Categories
    """
    __tablename__ = "Categories"
    __table_args__ = (
        UniqueConstraint(
            "category_code",
            name="uq_category_code"
        ),
        {"schema": settings.admin_db_schema},
    )
    id: int = Field(
        description="Category ID",
        title="Category ID",
        primary_key=True,
        sa_column=Column(
            nullable=False,
            comment="Category ID"
        )
    )
    category_code: str = Field(
        description="Category Code",
        title="Category Code",
        index=True,
        sa_column=Column(
            String(50),
            nullable=False,
            comment="Category Code"
        )
    )
    description: str | None = Field(
        default=None,
        description="Category Description",
        title="Category Description",
        sa_column=Column(
            String(255),
            nullable=True,
            comment="Category Description"
        )
    )

    groups: list["AccessGroups"] = Relationship(
        back_populates="categories",
        link_model=CategoriesAccess
    )
