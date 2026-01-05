from fastapi import FastAPI
from app.services.ebay import fetch_sold_listings
from app.services.pricing import calculate_market_price

app = FastAPI(title="Pokemon Card Price Comparator")

@app.get("/FetchSoldListingsService")
def service_fetch_listings(card_name: str):
    return {"status": "ok"}

@app.get("/PricingService")
def get_price(card_name: str, fee: float = 1):
    listings = fetch_sold_listings(card_name)
    result = calculate_market_price(listings)
    return result
