def planeRideCost(city):
	if city == "Charlotte":
		return 183
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 475

def rentalCarCost(days):
	rental_cost = days*40
	if days >= 3 and days < 7:
		rental_cost = rental_cost - 20
	elif days >= 7:
		rental_cost = rental_cost - 50
	
	return rental_cost

print rentalCarCost(4)
