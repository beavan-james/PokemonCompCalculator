#Pricing Service
#Fee is a multiplier for how much the user wants to pay based on the comp e.g. 70% of avg comps
def PricingService(soldlistings, activelistings, fee = 1):
   soldlistings = soldlistings.sort()
   min = soldlistings[0]
   max = soldlistings[-1]
   avg = sum(soldlistings) / len(soldlistings)
   price=0
   activeavg = sum(activelistings) / len(activelistings)
   if activeavg > avg:
         trend = "Stable"
   elif activeavg < avg:
         trend = "Falling"
   price = pricecalc(avg, trend, fee)
   return price

def pricecalc(avg, trend, fee):
   if trend == "Stable":
        pass
   elif trend == "Falling":
        avg = avg * 0.95
   price = avg * fee
   return price