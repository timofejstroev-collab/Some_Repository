test:
    uv run pytest -svv

#---

lint: mypy ruff-lint

mypy:
    uv run mypy main.py

ruff-lint:
    uv run ruff check --fix

#---

fmt: ruff-fmt

ruff-fmt:
    uv run ruff format

#---

start:
    uvicorn src.transports.http_fastapi.app:app --host 127.0.0.1 --port 8000 --reload