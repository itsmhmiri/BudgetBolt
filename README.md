# BudgetBolt - Freelancer Finance Tracker

## Project Overview

BudgetBolt is a modern, intuitive personal finance tracker specifically designed for freelancers and independent contractors. Unlike generic budgeting apps, BudgetBolt addresses the unique financial challenges freelancers face: irregular income, project-based payments, tax planning, and expense categorization for business purposes.

## Target Users

- Freelancers (developers, designers, writers, consultants)
- Independent contractors
- Gig economy workers
- Small business owners with project-based income

## Core Value Proposition

- **Irregular Income Management**: Handle variable monthly income with smart budgeting
- **Project-Based Tracking**: Link expenses and income to specific projects/clients
- **Tax Preparation**: Categorize expenses for easy tax filing
- **Cash Flow Forecasting**: Predict financial health with irregular payments
- **Modern UX**: Clean, intuitive interface that doesn't feel like traditional boring finance software

## Key Features

### 1. Dashboard & Overview

- Visual cash flow timeline showing income vs expenses
- Current month financial health score
- Upcoming payments and bills tracker
- Quick action buttons for common tasks
- Project profitability overview

### 2. Income Management

- Project-based income tracking
- Client payment management with due dates
- Invoice status tracking (sent, pending, paid, overdue)
- Income categorization (project work, recurring contracts, one-time gigs)
- Payment method tracking (bank transfer, PayPal, crypto, etc.)

### 3. Expense Tracking

- Smart expense categorization (office supplies, software subscriptions, travel, etc.)
- Project-specific expense allocation
- Receipt photo upload and OCR text extraction
- Recurring expense automation
- Business vs personal expense separation

### 4. Budgeting & Planning

- Flexible budgeting for irregular income
- "Worst case scenario" planning
- Emergency fund goal tracking
- Tax saving goals (quarterly tax payments)
- Equipment/software upgrade planning

### 5. Reports & Analytics

- Monthly/quarterly financial reports
- Tax-ready expense reports by category
- Client profitability analysis
- Expense trends and insights
- Profit margin tracking per project

### 6. Tax Features

- Tax-deductible expense highlighting
- Quarterly tax estimate calculator
- Tax document export (CSV, PDF)
- Mileage tracking for business travel
- Home office expense calculator

## Technical Architecture

### Selected Stack

- **Frontend**: React with modern hooks and context API
- **Backend**: Python FastAPI for robust API development
- **Database**: SQLite with SQLAlchemy ORM (simple deployment, suitable for personal use)
- **Authentication**: JWT tokens with secure httpOnly cookies
- **File Storage**: Local file system for receipts (with cloud option later)

### Why This Stack?

- **React**: Excellent ecosystem, component reusability, perfect for dashboard-heavy apps
- **FastAPI**: Fast development, automatic API docs, excellent type hints, perfect for rapid prototyping
- **SQLite**: Zero-config database, perfect for portfolio projects and single-user deployments

## Database Schema Overview

```
Users (id, email, password_hash, created_at)
Projects (id, user_id, name, client_name, hourly_rate, status)
Income (id, user_id, project_id, amount, date, description, status)
Expenses (id, user_id, project_id, amount, date, category, description, receipt_path, is_business)
Categories (id, name, type, tax_deductible)
Budgets (id, user_id, category_id, amount, period, created_at)
```

## UI/UX Design Principles

- **Modern & Clean**: Card-based layout, plenty of whitespace
- **Color Psychology**: Green for income, red for expenses, blue for budgets
- **Mobile-First**: Responsive design for on-the-go expense tracking
- **Data Visualization**: Charts and graphs for financial insights
- **Quick Actions**: Floating action button for rapid expense/income entry

---

# Cursor AI Agent Prompt

You are tasked with building "BudgetBolt" - a modern personal finance tracker specifically designed for freelancers. This is a full-stack web application that should feel professional and suitable for a developer portfolio.

## Project Requirements

### Tech Stack

- **Frontend**: React 18+ with TypeScript, Tailwind CSS for styling
- **Backend**: Python FastAPI with SQLAlchemy ORM and Pydantic models
- **Database**: SQLite for development (easy portfolio deployment)
- **Authentication**: JWT-based auth with secure httpOnly cookies

### Core Features to Implement

#### 1. Authentication System

- User registration and login
- JWT token management
- Protected routes
- Password hashing with bcrypt

#### 2. Dashboard (Main Page)

- Financial overview cards (total income, expenses, profit this month)
- Recent transactions list (last 10 entries)
- Quick stats: top expense categories, active projects
- Visual charts: monthly income vs expenses line chart
- Quick action floating button for adding income/expense

#### 3. Income Management

- Add/edit/delete income entries
- Fields: amount, date, project/client, description, payment status
- Income list with filtering and sorting
- Project-based income grouping

#### 4. Expense Tracking

- Add/edit/delete expense entries
- Fields: amount, date, category, description, project (optional), business/personal flag
- Expense categories: Office Supplies, Software, Travel, Equipment, Marketing, etc.
- Expense list with filtering by category, date range, project

#### 5. Projects Management

- Create/edit projects with client names
- Track project profitability (income vs expenses per project)
- Project status management (active, completed, on-hold)

#### 6. Reports Page

- Monthly summary reports
- Expense breakdown by category (pie chart)
- Income vs expenses over time (line chart)
- Tax-deductible expenses summary

### Technical Implementation Details

#### Frontend Structure

```
src/
├── components/
│   ├── common/ (Header, Sidebar, Modal, etc.)
│   ├── dashboard/ (DashboardCards, RecentTransactions, Charts)
│   ├── income/ (IncomeForm, IncomeList)
│   ├── expenses/ (ExpenseForm, ExpenseList, CategoryFilter)
│   └── projects/ (ProjectForm, ProjectCard)
├── pages/ (Dashboard, Income, Expenses, Projects, Reports, Auth)
├── hooks/ (useAuth, useAPI, useLocalStorage)
├── context/ (AuthContext, AppContext)
├── utils/ (api.js, formatters.js, validators.js)
└── types/ (TypeScript interfaces)
```

#### Backend Structure

```
app/
├── models/ (User, Income, Expense, Project, Category)
├── schemas/ (Pydantic models for request/response)
├── routers/ (auth, income, expenses, projects, reports)
├── database.py (SQLAlchemy setup)
├── auth.py (JWT utilities)
└── main.py (FastAPI app)
```

#### Key API Endpoints

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /dashboard/stats` - Dashboard summary data
- `GET/POST /income` - Income CRUD operations
- `GET/POST /expenses` - Expense CRUD operations
- `GET/POST /projects` - Project CRUD operations
- `GET /reports/monthly` - Monthly reports

### UI/UX Guidelines

- Use Tailwind CSS for modern, responsive design
- Implement dark/light mode toggle
- Card-based layout for main content
- Use Heroicons or Lucide React for consistent iconography
- Color scheme: Blue for primary actions, Green for income, Red for expenses
- Mobile-responsive design (mobile-first approach)
- Loading states and error handling for all async operations

### Data Validation & Security

- Input validation on both frontend and backend
- SQL injection prevention with SQLAlchemy ORM
- XSS protection with proper data sanitization
- CORS configuration for frontend-backend communication
- Rate limiting on API endpoints

### Development Priorities

1. Set up basic authentication system
2. Create main dashboard with summary cards
3. Implement income and expense CRUD operations
4. Add project management functionality
5. Build reports page with basic charts
6. Polish UI/UX and add responsive design
7. Add data validation and error handling

### Success Criteria

- Clean, professional-looking interface
- Smooth user experience with proper loading states
- All CRUD operations working correctly
- Responsive design that works on mobile
- Basic data visualization with charts
- Proper error handling and user feedback
- Code should be well-organized and documented for portfolio showcase

Build this as a production-ready application that demonstrates full-stack development skills, modern UI/UX design, and proper software architecture patterns.