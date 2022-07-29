from datetime import datetime
from rq_scheduler import Scheduler

from dependencies import get_redis
from tasks import check_payments

RUN_INTERVAL = 30


def create_scheduler():
    redis = get_redis()
    scheduler = Scheduler(connection=redis)
    scheduler.schedule(
        scheduled_time=datetime.utcnow(),
        func=check_payments,
        interval=RUN_INTERVAL,
    )
