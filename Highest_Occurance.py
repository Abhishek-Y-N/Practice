def occurance(arr):
	freq={}
	for i in arr:
		freq[i]=freq.get(i,0)+1
	high=arr[0]
	for i in freq:
		if freq[i]>freq[high]:
			high=i
		elif freq[i]==freq[high] and i<high:
			high=i

	return high 

l1=[1,1,2,3,4,4,4,5]
print(occurance(l1))

l2=[4,4,5,5,6]
print(occurance(l2))