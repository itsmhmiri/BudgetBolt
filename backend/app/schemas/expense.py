from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExpenseBase(BaseModel):
    amount: float
    date: datetime
    category_id: int
    description: Optional[str] = None
    project_id: Optional[int] = None
    is_business: bool = True
    receipt_path: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[datetime] = None
    category_id: Optional[int] = None
    description: Optional[str] = None
    project_id: Optional[int] = None
    is_business: Optional[bool] = None
    receipt_path: Optional[str] = None

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 