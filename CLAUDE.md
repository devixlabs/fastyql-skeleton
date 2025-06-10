# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a minimal FastAPI application with a single echo endpoint. The project uses Poetry for dependency management and is configured as a non-package project (`package-mode = false` in pyproject.toml).

## Development Commands

- Install dependencies: `poetry install`
- Run the server: `poetry run uvicorn main:app --host 0.0.0.0 --port 8000`
- Run with auto-reload for development: `poetry run uvicorn main:app --reload`

## Architecture

- **main.py**: Contains the FastAPI application with a single GET endpoint `/api/echo` that returns query parameters as JSON
- **pyproject.toml**: Poetry configuration with Python 3.10+ requirement and FastAPI/uvicorn dependencies
- Project is configured as non-installable (package-mode = false) since it's a simple script-based application