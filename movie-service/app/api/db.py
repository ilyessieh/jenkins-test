import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

#DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_URI = 'postgresql://movie_db_username:movie_db_password@postgres-movie:5432/movie_db_dev'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts_id', ARRAY(Integer))
)

database = Database(DATABASE_URI)