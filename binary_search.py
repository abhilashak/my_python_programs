import sys

def binary_search(list1,element):
    """ Apply binary search to the list list1 to find the 'element' """
    begin = 0
    end = (len(list1) - 1)
    if(begin >= end):
	print "Not found"
	sys.exit(0)
    mid = (begin + end) / 2
    if(element > list1[mid]):
     	binary_search(list1 [(mid+1): ],element)
    elif(element < list1 [mid]):
	binary_search(list1 [ :mid], element)
    elif(element == list1 [mid]):
	print "Element Found" 
    else:
	print "Not found"	
    return ""

print binary_search( [23,26,29,32,36,38,45,50], 26)
	
