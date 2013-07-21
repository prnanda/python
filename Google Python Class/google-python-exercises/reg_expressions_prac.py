import re

def Find(str,pat):
	print re.findall(str,pat)
	

Find(r'[\w.]+@[\w.]+', 'nick.p@gmail.com abc 12133 abcd@yahoo.com')
