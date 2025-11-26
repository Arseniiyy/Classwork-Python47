from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class TodoStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1,max_length=200)
    description: Optional[str] = Field(None, max_length=1000,description="Описание")
    status: TodoStatus = Field(default=TodoStatus.PENDING, description="Статус")

class TodoCreate(BaseModel):
    pass

class TodoUpadate(BaseModel):
    title: Optional[str] = Field(None, min_length=1,max_length=200)
    description:Optional[str] = Field(None, max_length=1000)
    status:Optional[TodoStatus] = None

class TodoIntDB(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class TodoResponse(TodoIntDB):
    """"Модель для ответа API(то,что возвращаем клиенту)"""
    pass