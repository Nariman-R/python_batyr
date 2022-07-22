from peewee import *
from environs import Env

environment = Env()
environment.read_env()

DB_NAME = environment('DB_NAME')
DB_URI = environment('DB_URI')

def get_db():
    db = PostgresqlDatabase(
        database=DB_NAME,
        dsn=DB_URI,
    )
    db.connect()

    return db
