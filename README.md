# template-py

A Python project template with modern tooling and best practices.

## Features

- Python 3.12+ support
- Ruff for linting and formatting
- UV for fast dependency management
- Pre-commit hooks for code quality
- Pytest for testing
- Pre-configured code quality rules

## Getting Started

### Install Dependencies

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.
If you don't have UV installed:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation

```bash
git clone <repository-url>
cd template-py
uv sync
uv run pre-commit install
```

### Usage

```bash
# Run the application
uv run python main.py

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src

# Run tests in verbose mode
uv run pytest -v
```

## Project Structure

```
template-py/
├── src/
│   └── my_pkg/
│       └── my_lib.py         # Library module
├── tests/
│   └── test_my_lib.py        # Test files
├── main.py                   # Main application entry point
├── pyproject.toml            # Project configuration and dependencies
├── uv.lock                   # Locked dependencies
├── .pre-commit-config.yaml   # Pre-commit hooks configuration
└── README.md                 # This file
```

## License

Add your license information here.
