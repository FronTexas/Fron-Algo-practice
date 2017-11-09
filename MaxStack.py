class MaxStack: 

	def __init__(self):
		self.main_stack = Stack()
		self.max_stack = Stack()

	def push(self,e):
		self.main_stack.push(e)
		if not self.max_stack.peek() or self.max_stack.peek() <= e: 
			self.max_stack.push(e)

	def pop():
		if self.max_stack.peek() == self.main_stack.peek():
			self.main_stack.pop()
			return self.max_stack.pop()

		return self.main_stack.pop()

	def getMax():
		return self.max_stack.peek()

	def peek():
		return self.main_stack.peek()