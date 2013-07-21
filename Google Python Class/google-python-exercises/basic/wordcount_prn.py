"""1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
"""
def getval(tups):
	return tups[1]
	
def print_words(filename):
	f = open(filename, 'r+')
	all_data = f.read()
	
	all_data = all_data.lower()
	
	#print len(all_data)
	all_data = all_data.split()
	all_data = sorted(all_data)
	
	#print all_data
	
	new_data = []
	dict_wc = {}
	
	for word in all_data:
		if word in new_data:
			dict_wc[word] = dict_wc[word] + 1
			
		else:
			new_data.append(word)
			dict_wc[word] = int(1)
			
	#print dict_wc
    
	count =0
	for i in sorted(dict_wc.items(), key=getval, reverse = True):
		print count
		print i
		count+=1
		if count >= 20:
			break
			
	f.close()


	
print_words('alice.txt')