# Crypto Price Calculator API

A FastAPI application that calculates the USD value of cryptocurrency amounts using the CoinLayer API.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET /
Welcome message endpoint

### POST /calculate-price
Calculate the USD value of a cryptocurrency amount.

Request body:
```json
{
    "crypto_symbol": "BTC",
    "amount": 0.5
}
```

Response:
```json
{
    "crypto_symbol": "BTC",
    "amount": 0.5,
    "usd_price": 50000.00,
    "total_usd": 25000.00
}
```

## API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): `http://localhost:8000/docs`
- Alternative API docs (ReDoc): `http://localhost:8000/redoc`
