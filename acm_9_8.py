class PriorityQueue: 
	def __init__(self):
		self.queue = []
	
	def __len__(self):
		return len(self.queue)

	def add(self,elm):
		self.queue.append(elm)
		self.queue.sort(key=lambda x: x['cost'],reverse=True)

	def pop(self):
		return self.queue.pop()

class Edge: 
	def __init__(self,value,start,end,time):
		self.value = value
		self.start = start
		self.end = end
		self.time = time
	
	def toString(self):
		return str((self.value,self.start,self.end,self.time))


class Graph:
  def __init__(self):
  	self.nodes = set([])
  	self.graph = {}

  def add_node(self,new_node):
  	self.nodes.add(new_node)


  def add_edge(self,from_node,to_node,start,end,time):
  	if from_node in self.graph:
  		self.graph[from_node].append(Edge(to_node,start,end,time))
  	else: 
  		self.graph[from_node] = [Edge(to_node,start,end,time)]

  def get_shortest_path(self,start,end):
  	distance_dict = {(start,start) : 0}
  	queue = PriorityQueue()
  	queue.add({'value':Edge(start,0,0,0),'cost':0})
  	visited = set([])

  	while len(queue):
  		current = queue.pop()
  		current_edge = current['value']
  		cost_to_current_node = current['cost']
  		visited.add(current_edge)
  		if current_edge.value in self.graph:
	  		neighbors = self.graph[current_edge.value]
	  		for neighbor in neighbors:
	  			if neighbor not in visited: 
	  				if cost_to_current_node < neighbor.end:
	  					if neighbor.start > cost_to_current_node:
			  				next_cost = neighbor.start + neighbor.time
			  			else:
			  				next_cost = cost_to_current_node + neighbor.time
			  			if (start,neighbor.value) in distance_dict:
			  				if next_cost < distance_dict[(start,neighbor.value)]:
			  					distance_dict[(start,neighbor.value)] = next_cost
			  					queue.add({'value':neighbor,'cost':distance_dict[(start,neighbor.value)]})
			  			else: 
			  				distance_dict[(start,neighbor.value)] = next_cost
			  				queue.add({'value':neighbor,'cost':distance_dict[(start,neighbor.value)]})
	if (start,end) not in distance_dict: 
		return "TRAPPED!" 
	else: 
		return distance_dict[(start,end)]

graph = Graph()
m,c = [int(e) for e in raw_input().split(' ')]
src,g = [e for e in raw_input().split(' ')]

for _m in range(m):
	raw_input()

for _c in range(c):
	a,b,s,e,t = raw_input().split(' ')
	graph.add_edge(a,b,int(s),int(e),int(t))

print graph.get_shortest_path(src,g)


