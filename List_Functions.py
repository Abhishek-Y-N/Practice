li=[10,20,30,40,50,60,70,80,90,99]

# Finding sum of last 4 Elements
print("Sum Of Last 4 Elements:",sum(li[-1:-5:-1]))	#using slice operation to get last 4 elements


#Finding Deffernce between maximun and minimum element in List

print("Difference in max and min element:",max(li)-min(li))


# inserting number at 6th position

num=li[3]/3		#getting 1/3 of 4 th element
li.insert(5,num)		#inserting new element at 6th position
print("After Inserion:",li)


#using above methods on Strings

s="Abhishek "

print("Max:",max(s))
print("Min:",min(s))
print("Sorted:",sorted(s))