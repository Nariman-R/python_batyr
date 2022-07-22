from pydantic import BaseModel

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
