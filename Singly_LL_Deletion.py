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

	#Function to Delete Node at given position
	def delete(self,pos):
		if pos==1:
			temp=self.head
			self.head=temp.next
		else:
			p=1
			temp=self.head
			while(p!=pos-1):
				temp=temp.next
				p+=1
			temp.next=temp.next.next

	#Display Linked List
	def display(self):
		temp=self.head
		while(temp):
			print(temp.data,end="->")
			temp=temp.next
		print("None")


li1=LinkedList()

li1.Create(Node(10))
li1.Create(Node(20))
li1.Create(Node(30))
li1.Create(Node(40))
li1.Create(Node(50))
li1.display()

print("Deleting  Node At 3")
li1.delete(3)
li1.display()

print("Deleting Head Node")
li1.delete(1)
li1.display()