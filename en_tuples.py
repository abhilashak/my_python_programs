def fun(list):
	""" Returns lists of tuples paired . """
	i=0
	while(i<(len(list)/2 + 1 )):
		list[i]=list[i],list[i+1]
		del list[i+1]
		i=i+1
	return list


m=fun([1,2,3,4,5,6])
print m




