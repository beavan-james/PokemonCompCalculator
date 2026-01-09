from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from app.services.ebay import fetch_sold_listings
from app.services.pricing import calculate_market_price
from app.models.price import compute_response
from app.services.cardinfo import card_statistics

app = FastAPI(title="Pokemon Card Price Comparator")

#For API test use /#Docs endpoint

class CardInfoResponse(BaseModel):
    message: str
    min: float
    max: float
    mean: float
    trend: str

class PastSoldListingsResponse(BaseModel):
    listings: List[float]

class PricingResponse(BaseModel):
    card_name: str
    price: str

@app.get("/CardInformationService", response_model=CardInfoResponse)
def card_info(card_name: str, limit: int = 25):
    card_name = card_name.lower()
    listings = fetch_sold_listings(card_name, limit)
    if not listings:
         raise HTTPException(status_code=404, detail="No sold listings found for the specified card.")
    response = card_statistics(listings)
    return response

@app.get("/PricingService", response_model=PricingResponse)
def get_price(card_name: str, fee: float = 1, limit: int = 25):
    card_name = card_name.lower()
    listings = fetch_sold_listings(card_name, limit)
    if not listings:
         raise HTTPException(status_code=404, detail="No sold listings found for the specified card.")
    price = calculate_market_price(listings, fee)
    response = compute_response(card_name, price)
    return response

@app.get("/pastsoldlisting", response_model=PastSoldListingsResponse)
def past_sold_listings(card_name: str, limit: int = 25):
    card_name = card_name.lower()
    listings = fetch_sold_listings(card_name, limit)
    if not listings:
         raise HTTPException(status_code=404, detail="No sold listings found for the specified card.")
    return {"listings": listings}