from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, Boolean, JSON, ForeignKey
from utilities.settings import settings


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class APIMethods(SQLModel, table=True):
    __tablename__ = "APIMethods"
    __table_args__ = {"schema": settings.admin_db_schema}

    id: int = Field(default=None, primary_key=True)
    api_router_id: int = Field(
        description="API Router ID",
        title="API Router ID",
        sa_column=Column(
            ForeignKey(
                f"{settings.admin_db_schema}.APIRouters.id",
                ondelete="CASCADE"
            ),
            nullable=False,
            comment="API Router ID"
        )
    )
    method_type: HTTPMethod = Field(
        description="Method Type",
        title="Method Type",
        sa_column=Column(
            String(10),
            nullable=False,
            comment="Method Type"
        )
    )
    operation_id: str = Field(
        description="Operation ID",
        title="Operation ID",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="Operation ID"
        )
    )
    summary: str = Field(
        description="Summary",
        title="Summary",
        sa_column=Column(
            String(255),
            nullable=False,
            comment="Summary"
        )
    )
    description: str = Field(
        description="Description",
        title="Description",
        sa_column=Column(
            String(1000),
            nullable=True,
            comment="Description"
        )
    )
    deprecated: bool = Field(
        description="Deprecated",
        title="Deprecated",
        default=False,
        sa_column=Column(
            Boolean,
            nullable=False,
            comment="Deprecated"
        )
    )
    rate_limit: int = Field(
        description="Rate Limit",
        title="Rate Limit",
        sa_column=Column(
            nullable=True,
            comment="Rate Limit"
        )
    )

    api_router: "APIRouters" = Relationship(
        back_populates="api_methods"
    )