from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.database import get_db
from app.auth import get_current_user
from app.models.user import User
from app.models.income import Income
from app.models.project import Project
from app.schemas.income import IncomeCreate, IncomeUpdate, IncomeResponse

router = APIRouter()

@router.post("/", response_model=IncomeResponse)
async def create_income(
    income_data: IncomeCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new income entry."""
    # Verify project exists and belongs to user if project_id is provided
    if income_data.project_id:
        project = db.query(Project).filter(
            Project.id == income_data.project_id,
            Project.user_id == current_user.id
        ).first()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
    
    db_income = Income(
        **income_data.dict(),
        user_id=current_user.id
    )
    
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    
    return db_income

@router.get("/", response_model=List[IncomeResponse])
async def get_incomes(
    skip: int = 0,
    limit: int = 100,
    project_id: Optional[int] = None,
    status: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get income entries with optional filtering."""
    query = db.query(Income).filter(Income.user_id == current_user.id)
    
    if project_id:
        query = query.filter(Income.project_id == project_id)
    
    if status:
        query = query.filter(Income.status == status)
    
    if start_date:
        query = query.filter(Income.date >= start_date)
    
    if end_date:
        query = query.filter(Income.date <= end_date)
    
    incomes = query.offset(skip).limit(limit).all()
    return incomes

@router.get("/{income_id}", response_model=IncomeResponse)
async def get_income(
    income_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific income entry."""
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()
    
    if not income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    
    return income

@router.put("/{income_id}", response_model=IncomeResponse)
async def update_income(
    income_id: int,
    income_data: IncomeUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update an income entry."""
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()
    
    if not income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    
    # Verify project exists and belongs to user if project_id is being updated
    if income_data.project_id:
        project = db.query(Project).filter(
            Project.id == income_data.project_id,
            Project.user_id == current_user.id
        ).first()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
    
    # Update fields
    update_data = income_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(income, field, value)
    
    db.commit()
    db.refresh(income)
    
    return income

@router.delete("/{income_id}")
async def delete_income(
    income_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete an income entry."""
    income = db.query(Income).filter(
        Income.id == income_id,
        Income.user_id == current_user.id
    ).first()
    
    if not income:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found"
        )
    
    db.delete(income)
    db.commit()
    
    return {"message": "Income deleted successfully"} 