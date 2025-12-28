#FetchSoldListingsService.py

def FetchSoldListingsService(ebay_api_client, user_id, card_name, start_date, end_date):
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
    sold_listings = []
    page_number = 1
    has_more_pages = True

    while has_more_pages:
        response = ebay_api_client.get_sold_listings(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            page_number=page_number
        )

        sold_listings.extend(response['listings'])

        has_more_pages = response['has_more_pages']
        page_number += 1

    return sold_listings