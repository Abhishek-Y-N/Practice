students={
	101:{"Name":"Aditi","Score":[78,85.90]},
	102:{"Name":"Rahul","Score":[45,60,50]},
	103:{"Name":"Sneha","Score":[90,88,95]},
	104:{"Name":"Karan","Score":[55,72,68]},
	105:{"Name":"Priya","Score":[48,69,88]},
	106:{"Name":"stud1","Score":[10,20,30]}
}

#calculate avg
for sid ,details in students.items():
	avg=sum(details["Score"])/len(details["Score"])
	details["Average"]=avg
	details["Passsed"]=avg>=50

#passed student info
print("Students Who Passed:")
for sid,details in students.items():
	if details["Passsed"]:
		print(details["Name"])

