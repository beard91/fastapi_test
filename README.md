# FastAPI Test Project

This is a simple FastAPI project designed for testing and experimentation purposes.

## Project Structure

```
api/
    __init__.py
    main.py
    __pycache__/
```

- `api/main.py`: The main entry point for the FastAPI application.
- `api/__init__.py`: Marks the `api` directory as a Python package.

## Requirements

- Python 3.9 or higher
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd fastapi_test
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn api.main:app --reload
   ```

2. Open your browser and navigate to:
   - API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Alternative API documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Features

- **Interactive API Documentation**: Automatically generated Swagger UI and ReDoc.
- **Lightweight and Fast**: Built with FastAPI, a modern web framework for Python.
