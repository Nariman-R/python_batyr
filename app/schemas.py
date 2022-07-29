from datetime import datetime
from pydantic import BaseModel, validator
from typing import Optional


MAX_PRICE = 10000


class ItemRequestSchema(BaseModel):
    title: str
    price: float
    category: str
    image_url: str
    description: str

    @validator("price")
    def price_more_than_max(cls, value: float):
        if value > MAX_PRICE:
            raise ValueError('payment sum is more than 10 000')
        return value


class ItemResponseSchema(ItemRequestSchema):
    id: int

    class Config:
        orm_mode = True


class ItemUpdateSchema(BaseModel):
    title: Optional[str]
    price: Optional[float]
    category: Optional[str]
    image_url: Optional[str]
    description: Optional[str]

    @validator("price")
    def price_more_than_max(cls, value: float):
        if value > MAX_PRICE:
            raise ValueError('payment sum is more than 10 000')
        return value


class PaymentRequestSchema(BaseModel):
    item_id: Optional[int]
    date: Optional[datetime]
    status: Optional[str]
    is_issued: Optional[bool]


class PaymentResponseSchema(PaymentRequestSchema):
    id: int

    class Config:
        orm_mode = True
