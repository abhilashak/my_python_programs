def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def reducee(fun,list):
	""" Acts like python reduce function"""
	i=0
	sum=0
	while(i<len(list)):
		sum=fun(sum,list[i])
		i=i+1
	return sum

print reducee (add,range(1,11))

	

