from fastapi import FastAPI
from app.ebay import fetch_sold_listings
from app.pricing import calculate_market_price

app = FastAPI(title="Pokemon Card Price Comparator")

@app.get("/FetchSoldListingsService")
def FetchSoldListingsService(ebay_api_client, user_id, card_name, start_date, end_date):
    return {"status": "ok"}

@app.get("/PricingService")
def get_price(card_name: str, fee: float = 1):
    listings = fetch_sold_listings(card_name)
    result = calculate_market_price(listings)
    return result

