def recmultiplation(n,p,result = 0):
	result = result + n
	if p != 1:
		p = p - 1
		return recmultiplation(n,p,result)
	elif p == 1: 
		return result
print recmultiplation(5,3)
L = [3,20,2,15,11,5,9,4,1]
def recfindmaxinlist(list,max = 0,i = 0):
	while len(list) > i:
		if list[i] > max:
			max = list[i]
			i = i + 1
			return recfindmaxinlist(list,max,i)
		else:
			i = i + 1
			return recfindmaxinlist(list,max,i)
	return max
def maxlist(list):
	if len(list) == 1:
		return list[0]
	else:
		m = maxlist(list[1:])
		if m > list[0]:
			return m
		else:
			return list[0]
print max(L)