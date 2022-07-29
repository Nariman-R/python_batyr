from environs import Env
from redis import Redis
from rq import Queue
from peewee import *


environment = Env()
environment.read_env()

DATABASE_NAME = environment("DATABASE_NAME")
DATABASE_URL = environment("DATABASE_URL")

REDIS_URL = environment("REDIS_URL")


def get_db():
    db = PostgresqlDatabase(
        database=DATABASE_NAME,
        dsn=DATABASE_URL,
    )
    db.connect()

    return db


def get_redis():
    redis = Redis.from_url(url=REDIS_URL)

    return redis


def get_queue():
    redis = get_redis()
    queue = Queue(connection=redis)

    return queue
