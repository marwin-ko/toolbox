class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)

# This data structure is called a Queue. It follows the ordering prinicpal called FIFO, first-in first-out. Think of a Queue as a line at the grocery store. First person in line gets served and so on; assuming no rude people cut in line.  
