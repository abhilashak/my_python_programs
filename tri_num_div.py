def next_num(index):
	return sum(range(index))
def factors(num):
	count = 0
	i = 2 
	count = 1
	if(num == 1):
		return 1
	elif(num > 1):
		count = count+1
		while(i < ((num/2) +1)):
			if((num % i) == 0):
				count= count+1	
			i += 1
	return count	

def tri_num():
	"""Shows the triangle number which has over 123 divisors"""
	num = 1
	index = 1
	while True:
		if((factors(num)) > 123):
			return  num
		num = next_num(index)
		index += 1
	

print tri_num()	
