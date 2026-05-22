pre-commit:
    uv run pre-commit run --all-files

hooks:
    uv run pre-commit install

check:
    format lint type-check pre-commit
