# BudgetBolt Backend

FastAPI backend for the BudgetBolt personal finance tracker application.

## Features

- **Authentication**: JWT-based authentication with secure password hashing
- **Income Management**: Track project-based income with payment status
- **Expense Tracking**: Categorize expenses with business/personal flags
- **Project Management**: Manage client projects with profitability tracking
- **Financial Reports**: Generate monthly reports and analytics
- **File Upload**: Receipt storage for expense tracking

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database (perfect for portfolio projects)
- **Pydantic**: Data validation using Python type annotations
- **JWT**: JSON Web Tokens for authentication
- **Pytest**: Testing framework

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment setup**:
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

3. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**:
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user info

### Income
- `GET /income` - List income entries
- `POST /income` - Create income entry
- `GET /income/{id}` - Get specific income
- `PUT /income/{id}` - Update income entry
- `DELETE /income/{id}` - Delete income entry

### Expenses
- `GET /expenses` - List expense entries
- `POST /expenses` - Create expense entry
- `GET /expenses/{id}` - Get specific expense
- `PUT /expenses/{id}` - Update expense entry
- `DELETE /expenses/{id}` - Delete expense entry

### Projects
- `GET /projects` - List projects
- `POST /projects` - Create project
- `GET /projects/{id}` - Get specific project
- `PUT /projects/{id}` - Update project
- `DELETE /projects/{id}` - Delete project
- `GET /projects/{id}/profitability` - Get project profitability

### Reports
- `GET /reports/dashboard` - Dashboard statistics
- `GET /reports/monthly/{year}/{month}` - Monthly report
- `GET /reports/expense-breakdown` - Expense breakdown by category
- `GET /reports/income-trends` - Income trends over time

## Database Schema

The application uses SQLite with the following main tables:

- **users**: User accounts and authentication
- **projects**: Client projects and project details
- **income**: Income entries linked to projects
- **expenses**: Expense entries with categories
- **categories**: Expense categories with tax deductible flags

## Testing

Run tests with pytest:
```bash
pytest app/tests/
```

## Development

The application follows a clean architecture pattern:

```
app/
├── models/          # SQLAlchemy ORM models
├── schemas/         # Pydantic request/response models
├── routers/         # API route handlers
├── core/           # Configuration and core utilities
├── utils/          # Helper functions
└── tests/          # Test files
```

## Security Features

- Password hashing with bcrypt
- JWT token authentication
- CORS protection
- Input validation with Pydantic
- SQL injection prevention with SQLAlchemy ORM 