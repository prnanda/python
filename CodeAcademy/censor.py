def censor(text,word):
	text_split =  text.split()
	new_text = ""
	for i in range(len(text_split)):
		if text_split[i] == word:
			text_split[i] =  "*"*len(word)
		
	return " ".join(text_split)		
	
	
	
	
	
choice = "y"
while choice == "y":
	input1 = raw_input("Please enter a string: ")
	input1 = str(input1)
	input2 = raw_input("Please enter word to censor: ")
	input2 = str(input2)
	print censor(input1,input2)
	choice = raw_input("Continue?")