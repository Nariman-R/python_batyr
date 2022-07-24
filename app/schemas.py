from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional

from app.models import Item


MAX_PRICE = 10000


class ItemRequestSchema(BaseModel):
    title: str
    price: float
    category: str
    image_url: str
    description: str
    

class ItemResponseSchema(ItemRequestSchema):
    id: int

    class Config:
        orm_mode = True


class ItemUpdateSchema(BaseModel):
    id: int
    title: str
    price: float
    category: str
    image_url: str
    description: str


class PaymentRequestSchema(BaseModel):
    item_id: int
    date: Optional[datetime]
    status: Optional[str]
    is_issued: Optional[bool]

    @validator("item_id")
    def price_more_than_max(cls, value: int):
        item_for_sell = Item.get_by_id(value)
        if item_for_sell.price > MAX_PRICE:
            raise ValueError('payment sum is more than 10 000')
        return value


class PaymentResponseSchema(PaymentRequestSchema):
    id: int

    class Config:
        orm_mode = True
