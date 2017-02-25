class Stack(object):
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[len(self.items)-1]

# This data structure is called a Stack. It follows the ordering principle called LIFO, last-in first-out. Think of it as stacking dirty plates. Once you start cleaning the plates, you start from top aka the last plate you stacked on top.  
