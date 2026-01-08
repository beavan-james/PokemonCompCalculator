from fastapi import FastAPI, HTTPException
from app.services.ebay import fetch_sold_listings
from app.services.pricing import calculate_market_price
from app.models.price import compute_response
from app.services.cardinfo import card_statistics

app = FastAPI(title="Pokemon Card Price Comparator")

@app.get("/CardInformationService")
def card_info(card_name: str, limit: int = 25):
    card_name = card_name.lower()
    listings = fetch_sold_listings(card_name, limit)
    if not listings:
         raise HTTPException(status_code=404, detail="No sold listings found for the specified card.")
    response = card_statistics(listings)
    return response

@app.get("/PricingService")
def get_price(card_name: str, fee: float = 1, limit: int = 25):
    card_name = card_name.lower()
    listings = fetch_sold_listings(card_name, limit)
    if not listings:
         raise HTTPException(status_code=404, detail="No sold listings found for the specified card.")
    price = calculate_market_price(listings, fee)
    result = compute_response(card_name, price)
    return result

@app.get("/pastsoldlisting")
def past_sold_listings(card_name: str, limit: int = 25):
    card_name = card_name.lower()
    listings = fetch_sold_listings(card_name, limit)
    if not listings:
         raise HTTPException(status_code=404, detail="No sold listings found for the specified card.")
    return {"listings": listings}