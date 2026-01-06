from fastapi import FastAPI
from app.services.ebay import fetch_sold_listings
from app.services.pricing import calculate_market_price
from app.models.price import compute_response

app = FastAPI(title="Pokemon Card Price Comparator")

@app.get("/FetchSoldListingsService")
def service_fetch_listings(card_name: str):
    listings = fetch_sold_listings(card_name)
    return {"listings": listings}

@app.get("/PricingService")
def get_price(card_name: str, fee: float = 1):
    listings = fetch_sold_listings(card_name)
    price = calculate_market_price(listings, fee)
    result = compute_response(card_name, price)
    return result

#test