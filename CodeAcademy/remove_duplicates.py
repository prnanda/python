def remove_duplicates(list):
	list = sorted(list)
	new_list = []
	for i in range(len(list)):
		if list[i] not in new_list:
			new_list.append(list[i])
			
	return new_list
	

input = [1,4,6,7,3,1,8,3]	
print remove_duplicates(input)