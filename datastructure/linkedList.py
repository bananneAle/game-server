class LinkedListNode:
	def __init__(self, value=None):
		self.value = value
		self.next = None
		
	def setNext(next):
		self.next = next
	

class LinkedList:
	def __init__(self, head=None):
		self.head = head
		self.tail = head
		self.elem = 0

	def add(self, Node):
		if (not self.head):
			self.head = Node
			self.tail = Node
		else:
			self.tail.setNext(Node)
			self.tail = Node
	
	def pop(self):
		if (not head):
			return -1
		else:
			retVal = self.head
			self.head = self.head.next
			return retVal
