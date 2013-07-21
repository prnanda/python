score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10} 

def scrabble_score(word):
	word_1 = word.lower()
	score_tot = 0
	for i in range(len(word)):
		score_tot = score_tot + score[word_1[i]]
	
	return score_tot
	
	
choice = "y"
while choice == "y":
	input1 = raw_input("Please enter a string: ")
	input1 = str(input1)
	print scrabble_score(input1)
	choice = raw_input("Continue?")