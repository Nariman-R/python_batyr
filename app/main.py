from fastapi import FastAPI, Depends
from datetime import datetime

from app.dependencies import get_db
from app.schemas import ItemRequestSchema, ItemResponseSchema, ItemUpdateSchema
from app.schemas import PaymentResponseSchema, PaymentRequestSchema
from app.models import Item, Payment


app = FastAPI(dependencies=[Depends(get_db)])


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict:
    item = Item.get_by_id(item_id)

    response = ItemResponseSchema.from_orm(item)

    return response.dict()


@app.post("/items")
def create_item(item_body: ItemRequestSchema) -> dict:
    item = Item.create(
        title=item_body.title,
        price=item_body.price,
        category=item_body.category,
        image_url=item_body.image_url,
        description=item_body.description
    )

    response = ItemResponseSchema.from_orm(item)

    return response.dict()


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item_to_delete = Item.get_by_id(item_id)
    item_to_delete.delete_instance()
    
    return {'operation result': 'record deleted'}


@app.patch("/items/")
def update_item(item_body: ItemUpdateSchema):
    item_to_update = Item.get_by_id(item_body.id)
    item_to_update.title = item_body.title
    item_to_update.price = item_body.price
    item_to_update.category = item_body.category
    item_to_update.image_url = item_body.image_url
    item_to_update.description = item_body.description
    item_to_update.save()
    
    return {'operation result': 'record updated'}


@app.post("/payments", response_model=PaymentResponseSchema)
def create_payment(payment_body: PaymentRequestSchema) -> dict:
    payment = Payment.create(
        item_id=payment_body.item_id,
        date=datetime.now(),
        status='new'
    )

    response = PaymentResponseSchema.from_orm(payment)

    return response.dict()
