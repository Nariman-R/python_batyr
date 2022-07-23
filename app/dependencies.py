from peewee import *
from environs import Env

environment = Env()
environment.read_env()

DATABASE_NAME = environment('DATABASE_NAME')
DATABASE_URL = environment('DATABASE_URL')

def get_db():
    db = PostgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_URL,
    )
    db.connect()

    return db
