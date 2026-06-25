from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from app.models import Status

class OrderCreate(BaseModel):
    items: str
    quantity: int = Field(gt=0)

class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    items: str
    quantity: int
    status: Status
    time_created: datetime