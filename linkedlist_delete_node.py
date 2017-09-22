class node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	def getNext(self):
		return self.next

	def getValue(self):
		return self.value

class linkedlist:
	def __init__(self, value):
		self.head = node(value)

	def __str__(self):
		node = self.head
		s = str(node.getValue())
		if node.getNext() is None:
			return s
		while node.next is not None:
			s += " -> " + str(node.next.value)
			node = node.next
		return s

	def add(self,value):
	    head = self.head
	    while head.next is not None:
	        head = head.next
	    head.next = node(value)

	def delete(self, value):
		head = self.head
		while head.value == value:
			self.head = head.next
			head = self.head
		while head != None:
			if head.next.value == value:
				head.next = head.next.next
			head = head.next

a = linkedlist(2)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(2)
a.add(4)
a.add(2)
print a
a.delete(2)
print a
