from datetime import datetime, timedelta
from fastapi import FastAPI, Depends
from typing import List

from dependencies import get_db, get_queue
from scheduler import create_scheduler
from schemas import ItemRequestSchema, ItemResponseSchema, ItemUpdateSchema
from schemas import PaymentResponseSchema, PaymentRequestSchema
from models import Item, Payment
from tasks import fill_file_with_hw, check_payments, issue_paid_item

app = FastAPI(dependencies=[Depends(get_db)],
              on_startup=[create_scheduler])


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/items/{item_id}", response_model=ItemResponseSchema)
def get_item(item_id: int) -> dict:
    item = Item.get_by_id(item_id)

    response = ItemResponseSchema.from_orm(item)

    return response.dict()


@app.get("/items", response_model=List[ItemResponseSchema])
def get_items_list():
    items_list = Item.select()

    response = [ItemResponseSchema.from_orm(item) for item in items_list]

    return response


@app.post("/items", response_model=ItemResponseSchema)
def create_item(item_body: ItemRequestSchema) -> dict:
    item = Item.create(title=item_body.title,
                       price=item_body.price,
                       category=item_body.category,
                       image_url=item_body.image_url,
                       description=item_body.description)

    response = ItemResponseSchema.from_orm(item)

    return response.dict()


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item_to_delete = Item.get_by_id(item_id)
    item_to_delete.delete_instance()

    return {"operation result": "record deleted"}


@app.patch("/items/{item_id}")
def update_item(item_id: int, item_body: ItemUpdateSchema):
    item_to_update = Item.get_by_id(item_id)

    for key, value in item_body.dict(exclude_unset=True).items():
        setattr(item_to_update, key, value)

    item_to_update.save()

    return {"operation result": "record updated"}


@app.post("/payments", response_model=PaymentResponseSchema)
def create_payment(payment_body: PaymentRequestSchema) -> dict:
    payment = Payment.create(item_id=payment_body.item_id,
                             date=datetime.now(),
                             status="new")

    response = PaymentResponseSchema.from_orm(payment)

    return response.dict()


@app.post("/payments/{payment_id}")
def approve_payment(payment_id: int):
    paid_payment = Payment.get_by_id(payment_id)
    paid_payment.status = "paid"
    paid_payment.save()

    queue = get_queue()
    queue.enqueue(issue_paid_item, payment_id)

    return {"operation result": "payment processed"}


@app.get("/payments/{days}", response_model=List[PaymentResponseSchema])
def get_payments_list(days: int):
    start_day = datetime.now() - timedelta(days=days)
    payments_list = Payment.select().where(Payment.date >= start_day)

    response = [PaymentResponseSchema.from_orm(item) for item in payments_list]

    return response


@app.post("/run-task")
def run_task():
    queue = get_queue()
    queue.enqueue(fill_file_with_hw)

    return {}


@app.post("/check-new-payment")
def check_new_payments():
    queue = get_queue()
    queue.enqueue(check_payments)

    return {}
