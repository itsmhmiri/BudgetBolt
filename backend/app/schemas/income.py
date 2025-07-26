from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.income import PaymentStatus

class IncomeBase(BaseModel):
    amount: float
    date: datetime
    description: Optional[str] = None
    project_id: Optional[int] = None
    status: PaymentStatus = PaymentStatus.PENDING
    payment_method: Optional[str] = None

class IncomeCreate(IncomeBase):
    pass

class IncomeUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    project_id: Optional[int] = None
    status: Optional[PaymentStatus] = None
    payment_method: Optional[str] = None

class IncomeResponse(IncomeBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 