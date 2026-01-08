def card_statistics(soldlistings):
   soldlistings.sort() # sort() is in-place, do not assign it to the variable
   min = soldlistings[0]
   max = soldlistings[-1]
   avg = sum(soldlistings) / len(soldlistings)
   median = soldlistings[len(soldlistings)//2]
   price=0
   trend = "Stable" # Default value
   if median > avg:
         trend = "Stable"
   elif median < avg:
         trend = "Falling"
   return {"message": "Statistics calculated", "min": min, "max": max, "mean": avg, "trend": trend}