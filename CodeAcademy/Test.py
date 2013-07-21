def reverse(input):
	i = len(input)-1
	j = 0
	
	while i >=0:
		reversed[j] = input[i]
		i-=1
		j+=1
		
	return reversed

choice = "y"
while choice == "y":
	input1 = raw_input("Please enter a string: ")
	input1 = str(input1)
	print reverse(input1)
	choice = raw_input("Continue?")