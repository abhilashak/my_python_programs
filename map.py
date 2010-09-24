def sqr(x):
	return x*x
def cube(x):
	return x*x*x

def mappe(fun,list):
	""" Acts like python map function. """

	i=0
	result=[]
	while(i<len(list)):
		result.append(fun(list[i]))
		i=i+1
	return result

print mappe(cube,range(1,20))

		
