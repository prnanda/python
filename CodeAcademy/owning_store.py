prices = {"banana":4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15}

total =0

for fruit in prices and stock:
	print fruit
	print "price: " + str(prices[fruit])
	print "stock: " + str(stock[fruit])
	total = total + (prices[fruit]*stock[fruit])

print total