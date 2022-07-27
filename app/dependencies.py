import requests

from peewee import *
from environs import Env
from redis import Redis
from rq import Queue

environment = Env()
environment.read_env()

DATABASE_NAME = environment('DATABASE_NAME')
DATABASE_URL = environment('DATABASE_URL')

REDIS_URL = environment('REDIS_URL')

STOCK_URL = 'https://www.w3schools.com/python/demopage.php'


def get_db():
    db = PostgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_URL,
    )
    db.connect()

    return db

def get_queue():
    redis = Redis.from_url(url=REDIS_URL)
    queue = Queue(connection=redis)

    return queue
