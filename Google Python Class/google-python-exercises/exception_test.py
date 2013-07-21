def readf(c, intt):
	try:
		print c + intt
	except TypeError:
		print "Char & intt have different data types"
	
	print "End of function"
	
char = 22
intt = 33		
readf(char, intt)


	