def reverse(input):
	reversed = ""
	i = len(input)-1
	while i >=0:
		reversed = reversed + input[i] 
		i-=1
		
		
	return reversed

choice = "y"
while choice == "y":
	input1 = raw_input("Please enter a string: ")
	input1 = str(input1)
	print reverse(input1)
	choice = raw_input("Continue?")