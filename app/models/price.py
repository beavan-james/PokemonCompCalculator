#Basic Response Structure

def compute_response (card_name, price):
   if price is None:
       return {
           "card_name": card_name,
           "price": "Price not available"
       }
   elif price < 0:
       return {
           "card_name": card_name,
           "price": "Invalid price"
       }
   else:
       return {
           "card_name": card_name,
           "price": f"${price:.2f}"
       }




