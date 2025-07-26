from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

from app.routers import auth, income, expenses, projects, reports
from app.database import engine
from app.models import user, income as income_model, expense, project, category

# Create database tables
user.Base.metadata.create_all(bind=engine)
income_model.Base.metadata.create_all(bind=engine)
expense.Base.metadata.create_all(bind=engine)
project.Base.metadata.create_all(bind=engine)
category.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BudgetBolt API",
    description="A modern personal finance tracker for freelancers",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1"]
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(income.router, prefix="/income", tags=["Income"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])

@app.get("/")
async def root():
    return {"message": "Welcome to BudgetBolt API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 