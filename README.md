# GitHub Actions Unit Testing

[![Python CI Workflow (Build, Test, and Deploy with UV)](https://github.com/iristap/github-actions-unit-testing/actions/workflows/ci.yml/badge.svg)](https://github.com/iristap/github-actions-unit-testing/actions/workflows/ci.yml)

A demonstration project showcasing how to set up automated unit testing with GitHub Actions using Python and the `uv` package manager. This repo includes a simple calculator module with comprehensive unit tests and a CI/CD pipeline.

## Project Structure

```
github-actions-unit-testing/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD workflow
├── src/
│   └── some_package/
│       ├── __init__.py
│       └── calculator.py          # Calculator implementation
├── tests/
│   └── test_calculator.py         # Unit tests for calculator
├── main.py                        # Just main file
├── pyproject.toml                 # Project configuration
├── requirements.txt               # Python dependencies
└── README.md                      # README
```


## Installation

### uv

```bash
# Clone the repository
git clone https://github.com/iristap/github-actions-unit-testing.git
cd github-actions-unit-testing

uv ven
uv sync
```

## Running Tests

### Using unittest directly

```bash
# Run all tests
python -m unittest discover -s tests

# Run specific test file
python -m unittest tests.test_calculator

# Run with verbose output
python -m unittest discover -s tests -v
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and continuous deployment.

### Workflow Features

- **Automated Testing**: Runs on every push and pull request to the `main` branch
- **Matrix Testing**: Tests across Python 3.10 and 3.12
- **Fast Dependency Management**: Uses `uv` for quick package installation
- **Automated Deployment**: Deploys to production environment on successful main branch builds

### Workflow Steps

1. **Checkout**: Fetches repository code
2. **Setup Python**: Configures Python environment
3. **Install Dependencies**: Uses `uv` to create virtual environment and install dependencies
4. **Run Tests**: Executes unit tests using unittest
5. **Deploy** : Simulated deployment to production

To view the CI/CD pipeline status, check the [Actions tab](https://github.com/iristap/github-actions-unit-testing/actions) in the GitHub repository.

## Calculator Module

The calculator module (`src/some_package/calculator.py`) provides four basic arithmetic operations:

### Functions

- **`add(a, b)`**: Returns the sum of two numbers
- **`subtract(a, b)`**: Returns the difference between two numbers
- **`multiply(a, b)`**: Returns the product of two numbers
- **`divide(a, b)`**: Returns the quotient of two numbers (raises `ValueError` for division by zero)

## Incoming logging
if not lazy


