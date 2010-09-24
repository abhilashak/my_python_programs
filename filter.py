def fun(x):
	if(x%2 != 0 and x%3 !=0):
		return x
	else:
	 	return 0
 
def filt(f,list):
	""" Acts like python filter function"""

	i=0
	x=[]
	while(i<len(list)):
		y=f(list[i])
	        if(y != 0):	
			x.append(y)
		i=i+1	
	return x

print filt(fun,range(2,25))

