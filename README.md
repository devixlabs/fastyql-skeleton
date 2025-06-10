# FastyQL Skeleton

A minimal FastAPI echo server built with Poetry.

## Requirements

- Python 3.10+
- Poetry

## Setup

Install dependencies:
```bash
poetry install
```

## Running

Start the server:
```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Usage

The server provides a single GET endpoint at `/api/echo` that returns the query parameters as JSON.

Example:
```bash
curl "http://localhost:8000/api/echo?foo=bar&test=123"
```

Returns:
```json
{"foo": "bar", "test": "123"}
```

