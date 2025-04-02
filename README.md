# Crypto Price Calculator API

A FastAPI-based service that calculates the USD value of cryptocurrency amounts using the CoinLayer API.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

To start the API server:
```bash
python Api/main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`

## Testing

### Running the Test Suite

To run all tests:
```bash
pytest Tests/test_crypto.py -v  
```

## Code Quality and Security Checks

### Running Flake8

To check code style and potential errors:
```bash
flake8 API  
```

### Running Bandit (Security Linter)

To check for common security issues:
```bash
bandit -r Api/ -ll
```

### Running Detect-Secrets

To scan for secrets and API keys in the code:


1. Scan for secrets:
```bash
trufflehog .
```


## Project Structure

```
.
├── Api/
│   └── main.py          # Main API implementation
├── tests/
│   └── test_main.py     # Test suite
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Contributing

1. Create a new branch for your feature
2. Create PR
3. If Fails show up, refactor your code and try again


