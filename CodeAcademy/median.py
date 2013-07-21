def median(list):
	list = sorted(list)
	n = len(list)
		
	if n%2 != 0:
		median = list[int(n/2)]
	else:
		xyz =  list[int(n/2)] + list[int(n/2)-1]
		median = float(xyz)/2
	
	median = float(median)
	return median

input = [7,3,1,4]	
print median(input)