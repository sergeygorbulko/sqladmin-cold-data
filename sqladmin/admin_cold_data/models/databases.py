from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String, ForeignKey
from utilities.settings import settings


class Databases(SQLModel, table=True):
    __tablename__ = "Databases"
    __table_args__ = {"schema": settings.admin_db_schema}

    id: int = Field(primary_key=True)
    alias: str = Field(
        description="Database Alias",
        sa_column=Column(
            String(255),
            nullable=False,
            unique=True,
            comment="Database Alias"
        )
    )
    description: str = Field(
        description="Database Description",
        sa_column=Column(
            String(1000),
            nullable=True,
            comment="Database Description"
        )
    )
    connection_string: str = Field(
        description="Connection String",
        sa_column=Column(
            String(1000),
            nullable=False,
            comment="Connection String"
        )
    )

    views: "Views" = Relationship(back_populates="database")
