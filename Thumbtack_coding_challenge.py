class Program:
	def __init__(self):
		self.name_value_stores = {}
		self.value_counter_stores = {}
		self.commands = {
			"SET": lambda params: self.set(params),
			"GET": lambda params: self.get(params),
			"UNSET": lambda params: self.unset(params),
			"NUMEQUALTO": lambda params: self.numEqualTo(params),
			"END" : lambda params: exit(),
		}

	def incrementValueCount(self,value):
		if value in self.value_counter_stores: 
			self.value_counter_stores[value] = self.value_counter_stores[value] + 1
		else: 
			self.value_counter_stores[value] = 1

	def decrementValueCount(self,value):
		if value in self.value_counter_stores:
			self.value_counter_stores[value] -= 1
			if self.value_counter_stores[value] == 0 : 
				del self.value_counter_stores[value]

	def run(self,line):
		line_splitted = line.split(' ')
		command,params = line_splitted[0],line_splitted[1:]


		if command not in self.commands: 
			print "> Command is invalid!"
			return

		print line

		result = self.commands[command](params)
		
		if result != None: 
			print "> " + str(result)

	def set(self,params):
		if len(params) != 2: 
			return "Invalid Syntax: 'SET' must be followed by 'name' and 'value'"

		name,value = params[0],params[1]

		if name in self.name_value_stores:
			name_current_value = self.name_value_stores[name]
			self.decrementValueCount(name_current_value)
		self.incrementValueCount(value)

		self.name_value_stores[name] = value 

	def get(self,params):
		if len(params) != 1:
			return "Invalid Syntax: 'GET' must be followed by 'name'" 

		name = params[0]

		if name not in self.name_value_stores:
			return "NULL"

		return self.name_value_stores[name]

	def unset(self,params):
		if len(params) != 1:
			return "Invalid Syntax: 'UNSET' must be followed by 'name'" 

		name = params[0]
		if name not in self.name_value_stores:
			return "variable " + str(name) + " does not exists!"
		
		name_current_value = self.name_value_stores[name]
		self.decrementValueCount(name_current_value)
		del self.name_value_stores[name]

	def numEqualTo(self,params):
		if len(params) != 1:
			return "Invalid Syntax: 'NUMEQUALTO' must be followed by 'name'" 

		value = params[0]
		value_counter = self.value_counter_stores[value] if value in self.value_counter_stores else 0
		return value_counter


p = Program()
line = raw_input()
while(line):
	p.run(line)	
	line = raw_input()


