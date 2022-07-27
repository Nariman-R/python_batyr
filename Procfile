web: uvicorn main:app --app-dir=app --host=0.0.0.0 --port=${PORT}
worker: rq worker -P app -c dependencies
scheduler: rqscheduler --path=app -v --interval=30 --url=${REDIS_URL}