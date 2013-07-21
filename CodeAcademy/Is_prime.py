def is_prime(x):
		
	n = int(x/2)
	for i in range(2,n):
		if (x%i) == 0:
			pr =  False
			break
	else:
		pr = True
		
	if x<2:
		pr = False
	if x==2:
		pr = True
		
	return pr
		
number = raw_input("Enter number: ")
number = int(number)
print is_prime(number)
		
	