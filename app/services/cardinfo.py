def card_statistics(soldlistings):
   soldlistings.sort() # sort() is in-place, do not assign it to the variable
   min_price = soldlistings[0]
   max_price = soldlistings[-1]
   avg = sum(soldlistings) / len(soldlistings)
   median = soldlistings[len(soldlistings)//2]
   trend = "Stable" # Default value
   if median > avg:
         trend = "Stable"
   elif median < avg:
         trend = "Falling"
   if min_price is None or max_price is None or avg is None or median is None or trend is None:
       return {"message": "Insufficient data to calculate statistics"}
   return {"message": "Statistics calculated", "min": min_price, "max": max_price, "mean": avg, "trend": trend}