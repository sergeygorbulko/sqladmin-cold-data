from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from utilities.settings import settings
from models.api_methods import APIMethods


class APIRouters(SQLModel, table=True):
    __tablename__ = "APIRouters"
    __table_args__ = {"schema": settings.admin_db_schema}

    id: int = Field(primary_key=True)
    model: str = Field(
        description="API Model",
        title="API Model",
        sa_column=Column(
            String(255),
            nullable=False,
            unique=True,
            comment="API Model"
        )
    )
    router: str = Field(
        description="API Router",
        title="API Router",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="API Router"
        )
    )
    prefix: str = Field(
        description="Router Prefix",
        title="Router Prefix",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="Router Prefix"
        )
    )
    description: str = Field(
        description="Router Description",
        title="Router Description",
        sa_column=Column(
            String(1000),
            nullable=True,
            comment="Router Description"
        )
    )

    api_methods: list[APIMethods] = Relationship(
        back_populates="api_router"
    )
