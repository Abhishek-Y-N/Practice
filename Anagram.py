
def anagram(n1,n2):
	freq=[0]*10
	while(n1!=0):
		ld=n1%10
		freq[ld]+=1
		n1//=10

	while(n2!=0):
		ld=n2%10
		freq[ld]-=1
		n2//=10

	for i in range(len(freq)):
		if freq[i]!=0:
			return False
	return True

n1=1221
n2=1212

print("Is Anagram:",anagram(n1,n2))