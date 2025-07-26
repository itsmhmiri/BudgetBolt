from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class CategoryType(str, enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    type = Column(Enum(CategoryType), nullable=False)
    tax_deductible = Column(Boolean, default=False)
    description = Column(String, nullable=True)

    # Relationships
    expenses = relationship("Expense", back_populates="category") 