from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import Column, String, ForeignKey
from models.views_access import ViewsAccess
from utilities.settings import settings


class Views(SQLModel, table=True):
    __tablename__ = "Views"
    __table_args__ = (
        UniqueConstraint(
            "view_name",
            "model_name",
            name="uq_view_name_model_name"
        ),
        {"schema": settings.admin_db_schema}
    )
    id: int = Field(primary_key=True)
    view_name: str = Field(
        description="View name",
        sa_column=Column(
            String(100),
            nullable=False,
            comment="View name"
        )
    )
    model_name: str = Field(
        description="Model name",
        sa_column=Column(
            String(100),
            nullable=False,
            unique=True,
            comment="Model name"
        )
    )
    description: str = Field(
        description="View description",
        sa_column=Column(
            String(255),
            nullable=True,
            comment="View description"
        )
    )
    view_module_import_path: str = Field(
        description="View module import path",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="View model import path"
        )
    )
    sqlmodel_module_import_path: str = Field(
        description="SQLModel module import path",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="SQLModel module import path"
        )
    )
    confluence_url: str = Field(
        description="Confluence URL",
        sa_column=Column(
            String(2000),
            nullable=True,
            comment="Confluence URL"
        )
    )
    identity: str = Field(
        description="View identity",
        sa_column=Column(
            String(100),
            nullable=False,
            unique=True,
            comment="View identity"
        )
    )
    groups: list["AccessGroups"] = Relationship(
        back_populates="views",
        link_model=ViewsAccess
    )

    database_id: int = Field(
        description="Database ID",
        sa_column=Column(
            ForeignKey(
                f"{settings.admin_db_schema}.Databases.id",
                ondelete="CASCADE"
            ),
            nullable=False,
            comment="Database ID"
        )
    )
    database: "Databases" = Relationship(back_populates="view")
