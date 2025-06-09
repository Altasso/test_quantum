from ninja import Schema
from datetime import datetime

class PostSchema(Schema):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True

class PostCreateSchema(Schema):
    title: str
    content: str