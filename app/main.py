from fastapi import FastAPI
from app.ebay import fetch_sold_listings
from app.pricing import calculate_market_price

app = FastAPI(title="Pokemon Card Price Comparator")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/price")
def get_price(card_name: str):
    listings = fetch_sold_listings(card_name)
    result = calculate_market_price(listings)
    return result

