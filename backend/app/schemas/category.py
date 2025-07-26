from pydantic import BaseModel
from typing import Optional
from app.models.category import CategoryType

class CategoryBase(BaseModel):
    name: str
    type: CategoryType
    tax_deductible: bool = False
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[CategoryType] = None
    tax_deductible: Optional[bool] = None
    description: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True 