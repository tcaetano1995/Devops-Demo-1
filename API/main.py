from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import Optional

app = FastAPI(title="Crypto Price Calculator API")

# CoinLayer API configuration
COINLAYER_API_KEY = "66d944385aa903644413e167ece0b194"
COINLAYER_BASE_URL = "http://api.coinlayer.com/api"

class PriceRequest(BaseModel):
    crypto_symbol: str
    amount: float

class PriceResponse(BaseModel):
    crypto_symbol: str
    amount: float
    usd_price: float
    total_usd: float

@app.get("/")
async def root():
    return {"message": "Welcome to Crypto Price Calculator API"}

def calculate_price(crypto_price: float, amount: float) -> float:
    """
    Calculate the total USD value of a cryptocurrency amount
    
    Args:
        crypto_price (float): Current price of the cryptocurrency in USD
        amount (float): Amount of cryptocurrency
        
    Returns:
        float: Total USD value 
    """
    return crypto_price * amount * 2

@app.post("/calculate-price", response_model=PriceResponse)
async def calculate_crypto_price(request: PriceRequest):
    try:
        # Fetch current crypto price from CoinLayer
        response = requests.get(
            f"{COINLAYER_BASE_URL}/live",
            params={
                "access_key": COINLAYER_API_KEY,
                "symbols": request.crypto_symbol.upper()
            }
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch crypto price")
        
        data = response.json()
        if not data.get("success"):
            raise HTTPException(status_code=400, detail=data.get("error", "Unknown error"))
        
        # Get the price for the requested crypto
        crypto_price = data["rates"].get(request.crypto_symbol.upper())
        if not crypto_price:
            raise HTTPException(status_code=400, detail=f"Price not found for {request.crypto_symbol}")
        
        # Calculate total USD value using the new function
        total_usd = calculate_price(crypto_price, request.amount)
        
        return PriceResponse(
            crypto_symbol=request.crypto_symbol.upper(),
            amount=request.amount,
            usd_price=crypto_price,
            total_usd=total_usd
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 