#Node Structure
class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None 

	#Adding Nodes To LinkedList
	def Create(self,new_node):
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while(temp.next):
				temp=temp.next
			temp.next=new_node
	
	#Display Linked List
	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print("None")


li1=LinkedList()
n1=Node(10)
n2=Node(20)
li1.Create(n1)
li1.Create(n2)
li1.Create(Node(30))
li1.Create(Node(40))
li1.display()