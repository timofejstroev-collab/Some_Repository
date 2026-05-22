lint: ruff-lint

ruff-lint:
    uv run ruff check --fix

#---

fmt: ruff-fmt

ruff-fmt:
    uv run ruff format

