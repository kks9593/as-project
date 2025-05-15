from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

as_table = Table(
    "as_request",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("content", String),
    Column("status", String),
)
