from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import Column, String, ForeignKey
from utilities.settings import settings


class Models(SQLModel, table=True):
    __tablename__ = "Models"
    __table_args__ = (
        UniqueConstraint(
            "model_name",
            name="uq_models_model_name"
        ),
        {"schema": settings.admin_db_schema}
    )
    id: int = Field(
        description="Model ID",
        title="Model ID",
        primary_key=True,
        sa_column=Column(
            nullable=False,
            comment="Model ID"
        )
    )
    model_name: str = Field(
        description="Model name",
        title="Model name",
        index=True,
        sa_column=Column(
            String(100),
            nullable=False,
            unique=True,
            comment="Model name"
        )
    )
    description: str = Field(
        description="View description",
        title="View description",
        sa_column=Column(
            String(255),
            nullable=True,
            comment="View description"
        )
    )
    sqlmodel_module_import_path: str = Field(
        description="SQLModel module import path",
        title="SQLModel module import path",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="SQLModel module import path"
        )
    )
    confluence_url: str = Field(
        description="Confluence URL",
        title="Confluence URL",
        sa_column=Column(
            String(2000),
            nullable=True,
            comment="Confluence URL"
        )
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
    database: "Databases" = Relationship(back_populates="model")
    view: "Views" = Relationship(back_populates="model")
