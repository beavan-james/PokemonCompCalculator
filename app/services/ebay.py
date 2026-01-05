#FetchSoldListingsService.py
import requests

EBAY_APP_ID = "YOUR_EBAY_APP_ID"  # from developer.ebay.com


def FetchSoldListingsService(ebay_api_client, user_id, card_name, start_date, end_date):
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
    """
    Fetch sold listings for a given user within a specified date range.

    Parameters:
    ebay_api_client (EbayApiClient): An instance of the eBay API client.
    user_id (str): The eBay user ID whose sold listings are to be fetched.
    start_date (str): The start date for the date range in ISO 8601 format.
    end_date (str): The end date for the date range in ISO 8601 format.

    Returns:
    list: A list of sold listings.
    """
    soldlistings = []
    page_number = 1
    has_more_pages = True

    while has_more_pages:
        response = ebay_api_client.get_sold_listings(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            page_number=page_number
        )

        soldlistings.extend(response['listings'])

        has_more_pages = response['has_more_pages']
        page_number += 1

    return soldlistings