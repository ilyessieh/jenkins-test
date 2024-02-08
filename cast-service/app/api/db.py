import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

#DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_URI = "postgresql://cast_db_username:cast_db_password@postgres-cast:5432/cast_db_dev"

engine = create_engine(DATABASE_URI)
metadata = MetaData()

casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('nationality', String(20)),
)

database = Database(DATABASE_URI)