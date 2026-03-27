# FastAPI Logging Service

Small FastAPI service for creating and retrieving log entries during local testing.

## Features

- `GET /health` public health check
- `POST /logs` create a log entry
- `GET /logs` list all stored log entries
- `GET /logs/{log_id}` fetch a single log entry by ID
- Header-based API key protection for log endpoints
- In-memory storage for simple local development
- Interactive API docs from FastAPI at `/docs` and `/redoc`

## Project Structure

```text
api/
    __init__.py
    auth.py
    main.py
    schemas.py
LICENSE
README.md
requirements.txt
```

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/beard91/fastapi_test.git
cd fastapi_test
pip install -r requirements.txt
```

## Run Locally

```bash
python -m uvicorn api.main:app --reload
```

Useful local URLs:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Health check: `http://127.0.0.1:8000/health`

## Authentication

All `/logs` endpoints require an `x-api-key` header.

Demo key:

```text
mysecretkey
```

Example:

```text
x-api-key: mysecretkey
```

`GET /health` does not require authentication.

## API Endpoints

### `GET /health`

Returns:

```json
{
  "status": "ok"
}
```

### `POST /logs`

Creates a new log entry.

Request body:

```json
{
  "level": "INFO",
  "message": "Application started"
}
```

Allowed `level` values:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

Successful response:

```json
{
  "id": 1,
  "level": "INFO",
  "message": "Application started"
}
```

Possible error responses:

- `400` for an invalid log level
- `401` for a missing or invalid API key
- `422` for schema validation errors such as an empty message

### `GET /logs`

Returns all stored log entries:

```json
[
  {
    "id": 1,
    "level": "INFO",
    "message": "Application started"
  }
]
```

### `GET /logs/{log_id}`

Returns a single stored log entry by numeric ID.

If the log does not exist:

```json
{
  "detail": "Log not found"
}
```

## cURL Examples

Create a log entry:

```bash
curl -X POST "http://127.0.0.1:8000/logs" \
  -H "Content-Type: application/json" \
  -H "x-api-key: mysecretkey" \
  -d "{\"level\":\"INFO\",\"message\":\"Application started successfully\"}"
```

List all logs:

```bash
curl "http://127.0.0.1:8000/logs" \
  -H "x-api-key: mysecretkey"
```

Fetch one log:

```bash
curl "http://127.0.0.1:8000/logs/1" \
  -H "x-api-key: mysecretkey"
```

## Notes

- Data is stored in memory and is lost when the server restarts.
- The API key is hardcoded and intended for local testing only.

## License

See [LICENSE](LICENSE).
