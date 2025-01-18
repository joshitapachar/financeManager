# Personal Finance Manager

A simple backend system to help users manage their personal finances by tracking income, expenses, savings goals, and generating reports.

## Features

- **User Management**: Register and login with unique credentials.
- **Transaction Management**: Add, view, update, and delete financial transactions.
- **Category Management**: Add and manage custom transaction categories.
- **Savings Goals**: Set, track, and view progress towards financial goals.
- **Reports**: Generate spending patterns with category-wise breakdowns.
- **Data Persistence**: Stores data in a lightweight SQLite database.

## Tech Stack

- **Python**: Programming language.
- **Flask**: Web framework.
- **SQLAlchemy**: Database ORM.
- **SQLite**: Embedded database.

## Prerequisites

- Python 3.7 or later
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/joshitapachar/financeManager.git
   cd financeManager
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\\Scripts\\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application:
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser or test using curl/HTTP clients.

## API Endpoints

### User Management
- **POST** `/register`: Register a new user.
- **POST** `/login`: Login with email and password.

### Transaction Management
- **POST** `/transactions`: Add a transaction.
- **GET** `/transactions/<user_id>`: Get transactions for a user.

### Category Management
- **POST** `/categories`: Add a new category.
- **GET** `/categories/<user_id>`: Get categories for a user.

### Savings Goals
- **POST** `/savings`: Add a savings goal.
- **GET** `/savings/<user_id>`: Get savings goals for a user.

## Running Tests

1. Install `pytest`:
   ```bash
   pip install pytest
   ```

2. Run the test suite:
   ```bash
   pytest
   ```
