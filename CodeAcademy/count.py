def count(sequence, item):
	count_er =0
	for i in range(len(sequence)):
		if sequence[i] == item:
			count_er += 1
	
	return count_er
	
	
choice = "y"
while choice == "y":
	input1 = raw_input("Please enter a sequence: ")
	input2 = raw_input("Please enter an item: ")
	print count(input1,input2)
	choice = raw_input("Continue?")