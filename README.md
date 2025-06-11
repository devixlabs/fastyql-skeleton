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
./run.sh
```

## Usage

The server provides a single GET endpoint at `/api/echo` that returns the query parameters as JSON.

Examples:
```bash
curl "http://localhost:8000/api/echo?foo=bar&test=123"
```

Returns:
```json
{"foo": "bar", "test": "123"}
```

For GraphQL:
```bash
curl -X POST http://localhost:8000/graphql -H "Content-Type: application/json" -d '{"query": "{ echo(message: \"Hello GraphQL\") }"}'
curl -X POST http://localhost:8000/graphql -H "Content-Type: application/json" -d '{"query": "{ echo }"}'
curl -X GET "http://localhost:8000/graphql?query=%7B%20echo%20%7D"
curl -X GET "http://localhost:8000/graphql?query=%7B%20echo(message:%20%22Hello%20GET%20GraphQL%22)%20%7D" 
```

