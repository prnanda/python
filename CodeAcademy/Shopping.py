groceries = ["banana", "orange","apple"]

stock = {"banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }
    
prices = {"banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

def computeBill(food):
	bill = 0
	for i in range(len(food)):
		if stock[food[i]] != 0:
			stock[food[i]] -= 1
			bill = float(bill + prices[food[i]])
		    	
	return bill 
    
print computeBill(groceries)