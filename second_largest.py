def print2largest(self,arr, n):
	# code here
	#lets sort the array to get the highest value
	arr.sort()
	#lets assume that in array the last element will be the highest element
	mx = arr[-1]
# 	initializing the s_h (second heighest) as int() with no value becoz in future we are going to update it
	s_h = int()
# 	using loop so that to check the element,using index we will if that particular index element is lesser than mx value
	for i in range(1,n+1):
# 		if yes the update the s_h and break the loop
	    if arr[-i]<mx:
		s_h = arr[-i]
		break
# 		else print -1 as no second highest present in the array 
	    else: s_h = -1
	return s_h
