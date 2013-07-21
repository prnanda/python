def anti_vowel(text):
	#print lower_text
	vows = "aeiouAEIOU"
	new_str = ""
	
	for i in range(len(text)):
		if not(text[i] in vows):
			new_str = new_str + text[i]
		elif text[i] == " ":
			new_str = new_str + " "
				
	return new_str
			
	
choice = "y"
while choice == "y":
	input1 = raw_input("Please enter a string: ")
	input1 = str(input1)
	print anti_vowel(input1)
	choice = raw_input("Continue?")