def hashing(arr):
	freq=[0]*10
	for i in range(len(arr)):
		freq[arr[i]]+=1

	for i in range(len(freq)):
		print(f"{i}->{freq[i]}")

arr=[1,1,4,3,2,5,2]
hashing(arr)