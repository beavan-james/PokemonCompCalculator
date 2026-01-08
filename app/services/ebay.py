#FetchSoldListingsService.py
import requests

EBAY_APP_ID = "YOUR_EBAY_APP_ID"  # from developer.ebay.com


def fetch_sold_listings(card_name, limit=25):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"
    headers = {"X-EBAY-SOA-OPERATION-NAME": "findCompletedItems"}
    params = {
        "OPERATION-NAME": "findCompletedItems",
        "SERVICE-VERSION": "1.0.0",
        "SECURITY-APPNAME": EBAY_APP_ID,
        "RESPONSE-DATA-FORMAT": "JSON",
        "keywords": card_name,
        "itemFilter(0).name": "SoldItemsOnly",
        "itemFilter(0).value": "true",
        "paginationInput.entriesPerPage": "50"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    soldlistings = []
    
    # Parse eBay Finding API JSON response
    try:
        # Navigate: findCompletedItemsResponse -> searchResult -> item
        search_result = data.get('findCompletedItemsResponse', [{}])[0].get('searchResult', [{}])[0]
        items = search_result.get('item', [])
        while len(soldlistings) < limit:
            for item in items:
                # Extract price: sellingStatus -> currentPrice -> __value__
                price_str = item.get('sellingStatus', [{}])[0].get('currentPrice', [{}])[0].get('__value__')
                if price_str:
                    soldlistings.append(float(price_str))
    except (IndexError, ValueError, KeyError):
        pass # Return empty list if parsing fails
        
    return soldlistings