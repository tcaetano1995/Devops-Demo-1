
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import requests
import os

app = FastAPI(title="Crypto Price Calculator API")

COINLAYER_API_KEY = os.environ.get("COINLAYER_API_KEY")
if not COINLAYER_API_KEY:
    raise RuntimeError("Missing COINLAYER_API_KEY environment variable")
COINLAYER_BASE_URL = "http://api.coinlayer.com/api"


class PriceRequest(BaseModel):
    crypto_symbol: str
    amount: float

    @validator("crypto_symbol")
    def validate_symbol(cls, v):
        if not v.isalpha():
            raise ValueError("Symbol must contain only letters")
        return v.upper()

    @validator("amount")
    def validate_amount(cls, v):
        if v < 0:
            raise ValueError("must be non-negative")
        return v


class PriceResponse(BaseModel):
    crypto_symbol: str
    amount: float
    usd_price: float
    total_usd: float


def calculate_price(crypto_price: float, amount: float) -> float:
    """Calculate the total USD value of a cryptocurrency amount."""
    return crypto_price * amount


@app.post("/calculate-price", response_model=PriceResponse)
async def calculate_crypto_price(request: PriceRequest):
    try:
        response = requests.get(
            f"{COINLAYER_BASE_URL}/live",
            params={
                "access_key": COINLAYER_API_KEY,
                "symbols": request.crypto_symbol
            },
            timeout=5
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail="Failed to fetch crypto price"
            )

        data = response.json()
        if not data.get("success", False):
            raise HTTPException(
                status_code=400,
                detail=data.get("error", {}).get("info", "Unknown error from API")
            )

        crypto_price = data["rates"].get(request.crypto_symbol)
        if crypto_price is None:
            raise HTTPException(
                status_code=400,
                detail=f"Price not found for symbol: {request.crypto_symbol}"
            )

        total_usd = calculate_price(crypto_price, request.amount)

        return PriceResponse(
            crypto_symbol=request.crypto_symbol,
            amount=request.amount,
            usd_price=crypto_price,
            total_usd=total_usd
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
