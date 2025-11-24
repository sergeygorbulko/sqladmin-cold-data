from sqlmodel import SQLModel, Field, Column
from sqlalchemy import Integer, DateTime, String
from datetime import datetime
from utilities.settings import settings


class ImportsData(SQLModel, table=True):
    __tablename__ = "imports_data"

    id: int = Field(
        default=None,
        primary_key=True,
        sa_column=Column( 
            Integer, 
            autoincrement=True
        )
    )
    date_created: datetime = Field(
        description="Creation date",
        title="Creation Date",
        sa_column=Column(
            DateTime,
            nullable=False,
            comment="Record creation date",
        )
    )
    batch_size: int = Field(
        description="Batch size",
        title="Batch Size",
        sa_column=Column(
            Integer,
            nullable=False,
            comment="Number of records processed in each batch",
        )
    )
    count_rows: int = Field(
        description="Total count",
        title="Total Count",
        sa_column=Column(
            Integer,
            comment="Total number of records imported",
        )
    )
    count_rows_loaded: int = Field(
        description="Count of loaded rows",
        title="Count of Loaded Rows",
        sa_column=Column(
            Integer,
            comment="Number of records successfully loaded",
        )
    )
    bucket_mame: str = Field(
        description="Bucket name",
        title="Bucket Name",
        sa_column=Column(
            String,
            nullable=False,
            comment="Name of the storage bucket",
        )
    )
    file_name: str = Field(
        description="File name",
        title="File Name",
        sa_column=Column(
            String,
            nullable=False,
            comment="Name of the imported file",
        )
    )
    db_destination: str = Field(
        description="Database destination",
        title="Database Destination",
        sa_column=Column(
            String,
            nullable=False,
            comment="Target database for the import",
        )
    )
    table_destination: str = Field(
        description="Table destination",
        title="Table Destination",
        sa_column=Column(
            String,
            nullable=False,
            comment="Target table for the import",
        )
    )
    status: str = Field(
        description="Import status",
        title="Import Status",
        sa_column=Column(
            String,
            nullable=False,
            comment="Current status of the import process",
        )
    )
    info: str = Field(
        description="Additional info",
        title="Additional Info",
        sa_column=Column(
            String,
            comment="Additional information about the import",
        )
    )