from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from typing import List, Optional
from datetime import datetime, timedelta
from calendar import monthrange

from app.database import get_db
from app.auth import get_current_user
from app.models.user import User
from app.models.income import Income
from app.models.expense import Expense
from app.models.category import Category
from app.models.project import Project

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get dashboard summary statistics."""
    # Get current month
    now = datetime.now()
    start_of_month = datetime(now.year, now.month, 1)
    end_of_month = datetime(now.year, now.month, monthrange(now.year, now.month)[1], 23, 59, 59)
    
    # Monthly income
    monthly_income = db.query(func.sum(Income.amount)).filter(
        Income.user_id == current_user.id,
        Income.date >= start_of_month,
        Income.date <= end_of_month
    ).scalar() or 0.0
    
    # Monthly expenses
    monthly_expenses = db.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        Expense.date >= start_of_month,
        Expense.date <= end_of_month
    ).scalar() or 0.0
    
    # Monthly profit
    monthly_profit = monthly_income - monthly_expenses
    
    # Pending payments
    pending_payments = db.query(func.sum(Income.amount)).filter(
        Income.user_id == current_user.id,
        Income.status == "pending"
    ).scalar() or 0.0
    
    # Active projects count
    active_projects = db.query(func.count(Project.id)).filter(
        Project.user_id == current_user.id,
        Project.status == "active"
    ).scalar() or 0
    
    # Recent transactions (last 5)
    recent_income = db.query(Income).filter(
        Income.user_id == current_user.id
    ).order_by(Income.date.desc()).limit(5).all()
    
    recent_expenses = db.query(Expense).filter(
        Expense.user_id == current_user.id
    ).order_by(Expense.date.desc()).limit(5).all()
    
    return {
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
        "monthly_profit": monthly_profit,
        "pending_payments": pending_payments,
        "active_projects": active_projects,
        "recent_income": [
            {
                "id": income.id,
                "amount": income.amount,
                "date": income.date,
                "description": income.description,
                "status": income.status
            } for income in recent_income
        ],
        "recent_expenses": [
            {
                "id": expense.id,
                "amount": expense.amount,
                "date": expense.date,
                "description": expense.description,
                "category_id": expense.category_id
            } for expense in recent_expenses
        ]
    }

@router.get("/monthly/{year}/{month}")
async def get_monthly_report(
    year: int,
    month: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get detailed monthly financial report."""
    # Validate year and month
    if month < 1 or month > 12:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid month"
        )
    
    start_of_month = datetime(year, month, 1)
    end_of_month = datetime(year, month, monthrange(year, month)[1], 23, 59, 59)
    
    # Monthly totals
    total_income = db.query(func.sum(Income.amount)).filter(
        Income.user_id == current_user.id,
        Income.date >= start_of_month,
        Income.date <= end_of_month
    ).scalar() or 0.0
    
    total_expenses = db.query(func.sum(Expense.amount)).filter(
        Expense.user_id == current_user.id,
        Expense.date >= start_of_month,
        Expense.date <= end_of_month
    ).scalar() or 0.0
    
    # Expenses by category
    expenses_by_category = db.query(
        Category.name,
        func.sum(Expense.amount).label('total')
    ).join(Expense).filter(
        Expense.user_id == current_user.id,
        Expense.date >= start_of_month,
        Expense.date <= end_of_month
    ).group_by(Category.name).all()
    
    # Income by project
    income_by_project = db.query(
        Project.name,
        func.sum(Income.amount).label('total')
    ).join(Income).filter(
        Income.user_id == current_user.id,
        Income.date >= start_of_month,
        Income.date <= end_of_month
    ).group_by(Project.name).all()
    
    # Tax deductible expenses
    tax_deductible_expenses = db.query(func.sum(Expense.amount)).join(Category).filter(
        Expense.user_id == current_user.id,
        Expense.date >= start_of_month,
        Expense.date <= end_of_month,
        Category.tax_deductible == True
    ).scalar() or 0.0
    
    return {
        "year": year,
        "month": month,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_profit": total_income - total_expenses,
        "expenses_by_category": [
            {"category": name, "amount": float(total)} 
            for name, total in expenses_by_category
        ],
        "income_by_project": [
            {"project": name, "amount": float(total)} 
            for name, total in income_by_project
        ],
        "tax_deductible_expenses": tax_deductible_expenses
    }

@router.get("/expense-breakdown")
async def get_expense_breakdown(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get expense breakdown by category."""
    query = db.query(Expense).filter(Expense.user_id == current_user.id)
    
    if start_date:
        query = query.filter(Expense.date >= start_date)
    if end_date:
        query = query.filter(Expense.date <= end_date)
    
    expenses_by_category = db.query(
        Category.name,
        Category.tax_deductible,
        func.sum(Expense.amount).label('total'),
        func.count(Expense.id).label('count')
    ).join(Expense).filter(
        Expense.user_id == current_user.id
    )
    
    if start_date:
        expenses_by_category = expenses_by_category.filter(Expense.date >= start_date)
    if end_date:
        expenses_by_category = expenses_by_category.filter(Expense.date <= end_date)
    
    expenses_by_category = expenses_by_category.group_by(Category.name, Category.tax_deductible).all()
    
    return [
        {
            "category": name,
            "tax_deductible": tax_deductible,
            "total_amount": float(total),
            "transaction_count": count
        }
        for name, tax_deductible, total, count in expenses_by_category
    ]

@router.get("/income-trends")
async def get_income_trends(
    months: int = 6,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get income trends over the last N months."""
    now = datetime.now()
    trends = []
    
    for i in range(months):
        # Calculate month boundaries
        if now.month - i <= 0:
            year = now.year - 1
            month = 12 + (now.month - i)
        else:
            year = now.year
            month = now.month - i
        
        start_of_month = datetime(year, month, 1)
        end_of_month = datetime(year, month, monthrange(year, month)[1], 23, 59, 59)
        
        # Get income for this month
        monthly_income = db.query(func.sum(Income.amount)).filter(
            Income.user_id == current_user.id,
            Income.date >= start_of_month,
            Income.date <= end_of_month
        ).scalar() or 0.0
        
        trends.append({
            "year": year,
            "month": month,
            "income": monthly_income
        })
    
    return trends[::-1]  # Reverse to get chronological order 