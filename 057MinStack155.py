class MinStack:
	def __init__(self):
		self.q = []

	# @param x, an integer
	# @return an integer
	def push(self, x):
		curMin = self.getMin()
		if curMin == None or x < curMin:
			curMin = x
		self.q.append((x, curMin));

	# @return nothing
	def pop(self):
		self.q.pop()


	# @return an integer
	def top(self):
		if len(self.q) == 0:
			return None
		else:
			return self.q[len(self.q) - 1][0]


	# @return an integer
	def getMin(self):
		if len(self.q) == 0:
			return None
		else:
			return self.q[len(self.q) - 1][1]

	
class MinStack:
	# initialize your data structure here.
	def __init__(self):
		self.stack = []
		self.ordered = []

	# @param x, an integer
	# @return nothing
	def push(self, x):
		if self.getMin() == None:
			self.ordered.append(x)
		else:
			self.ordered.append(min(x,self.ordered[-1]))
		self.stack.append(x)
	# @return nothing
	def pop(self):
		self.stack.pop()
		self.ordered.pop()

	# @return an integer
	def top(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]

	# @return an integer
	def getMin(self):
		if len(self.stack) == 0:
			return None
		return self.ordered[-1]

a = 5
b = MinStack()
print len(b.stack)
c = b.getMin()
print c
c = b.push(a)
print b.getMin()
a = 6
c = b.push(a)
print b.stack
print b.ordered
