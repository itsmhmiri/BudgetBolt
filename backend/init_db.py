#!/usr/bin/env python3
"""
Database initialization script for BudgetBolt.
Creates default expense categories and sets up the database.
"""

from app.database import engine, SessionLocal
from app.models.category import Category, CategoryType
from app.models.user import User
from app.models.project import Project
from app.models.income import Income
from app.models.expense import Expense

def init_db():
    """Initialize the database with default data."""
    from app.database import Base
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if categories already exist
        existing_categories = db.query(Category).count()
        if existing_categories > 0:
            print("Categories already exist, skipping initialization.")
            return
        
        # Create default expense categories
        default_categories = [
            # Business expenses
            Category(name="Office Supplies", type=CategoryType.EXPENSE, tax_deductible=True, description="Office supplies and stationery"),
            Category(name="Software Subscriptions", type=CategoryType.EXPENSE, tax_deductible=True, description="Software and SaaS subscriptions"),
            Category(name="Equipment", type=CategoryType.EXPENSE, tax_deductible=True, description="Computers, phones, and other equipment"),
            Category(name="Travel", type=CategoryType.EXPENSE, tax_deductible=True, description="Business travel expenses"),
            Category(name="Marketing", type=CategoryType.EXPENSE, tax_deductible=True, description="Marketing and advertising costs"),
            Category(name="Professional Development", type=CategoryType.EXPENSE, tax_deductible=True, description="Courses, conferences, and training"),
            Category(name="Insurance", type=CategoryType.EXPENSE, tax_deductible=True, description="Business insurance"),
            Category(name="Legal & Accounting", type=CategoryType.EXPENSE, tax_deductible=True, description="Legal and accounting services"),
            Category(name="Home Office", type=CategoryType.EXPENSE, tax_deductible=True, description="Home office expenses"),
            Category(name="Internet & Phone", type=CategoryType.EXPENSE, tax_deductible=True, description="Internet and phone bills"),
            
            # Personal expenses
            Category(name="Food & Dining", type=CategoryType.EXPENSE, tax_deductible=False, description="Food and dining expenses"),
            Category(name="Transportation", type=CategoryType.EXPENSE, tax_deductible=False, description="Personal transportation costs"),
            Category(name="Entertainment", type=CategoryType.EXPENSE, tax_deductible=False, description="Entertainment and recreation"),
            Category(name="Healthcare", type=CategoryType.EXPENSE, tax_deductible=False, description="Healthcare and medical expenses"),
            Category(name="Shopping", type=CategoryType.EXPENSE, tax_deductible=False, description="Personal shopping and retail"),
            Category(name="Utilities", type=CategoryType.EXPENSE, tax_deductible=False, description="Home utilities"),
            Category(name="Rent/Mortgage", type=CategoryType.EXPENSE, tax_deductible=False, description="Housing costs"),
            
            # Income categories
            Category(name="Project Work", type=CategoryType.INCOME, tax_deductible=False, description="Income from project work"),
            Category(name="Recurring Contracts", type=CategoryType.INCOME, tax_deductible=False, description="Income from recurring contracts"),
            Category(name="Consulting", type=CategoryType.INCOME, tax_deductible=False, description="Consulting income"),
            Category(name="Other Income", type=CategoryType.INCOME, tax_deductible=False, description="Other sources of income"),
        ]
        
        for category in default_categories:
            db.add(category)
        
        db.commit()
        print(f"Created {len(default_categories)} default categories.")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing BudgetBolt database...")
    init_db()
    print("Database initialization complete!") 