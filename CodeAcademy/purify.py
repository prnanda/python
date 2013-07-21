def purify(list):
	new_list=[]
	for i in range(len(list)):
		if list[i] % 2 == 0:
			new_list.append(list[i])
	
	return new_list
	
	
