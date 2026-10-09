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

	# Function to insert Node at given postion
	def insert(self,new_node,pos):
		if pos==1:
			new_node.next=self.head 
			self.head=new_node
			print("Node Added Succesfully")
		else:
			p=1
			temp=self.head
			while(p!=pos-1):
				temp=temp.next
				p+=1 
			new_node.next=temp.next
			temp.next=new_node 
			print("Node Added Succesfully")

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

print("Insertion At Positon 3")
li1.insert(Node(90),3)
li1.display()

print("Insertion At Last Positon")
li1.insert(Node(50),5)
li1.display()