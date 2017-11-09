'''
	
	a = Vertex(a)
	a.add_neighbor(b,0,5,4)
	a.add_neighbor(c,0,5,4)
	---------------------------------
	a.adjacent = [(b,0,5,4),(c,0,5,4)]
	---------------------------------
	c.add_neighbor()
	
'''

class PriorityQueue: 
	def __init__(self):
		self.queue = []
		self.sort_func = lambda x : x

	def __len__(self):
		return len(self.queue)

	def setSortingFunction(self,sort_func):
		self.sort_func = sort_func

	def pop(self):
		return self.queue.pop()

	def add(self,value):
		self.queue.append(value)
		self.queue.sort(key=self.sort_func,reverse=True)

class Connection: 
	def __init__(self,machine,s,e,t):
		self.machine = machine
		self.start = s 
		self.end = e 
		self.time = t

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self,machine,s,e,t):
        self.adjacent.append(Connection(machine,s,e,t))

    def get_adjacents(self):
        return self.adjacent

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, s,e,t):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], s,e,t)

    def get_vertices(self):
        return self.vert_dict.keys()

    def dijkstra(self,start,end):
    	shortest_path = {}
    	pq = PriorityQueue()
    	pq.setSortingFunction(lambda x:x['cost'])
    	pq.add({'connection':Connection(start,0,0,0),'cost':0})
    	visited = set([])
    	while len(pq):
    		current = pq.pop()
    		connection,cost = current['connection'] , current['cost']
    		visited.add(connection)
    		adjacents = vert_dict[connection.machine].get_adjacents()

    		for adjacent in adjacents:
    			machine = adjacent.machine
    			start = adjacent.start
    			end = adjacent.end 
    			time = adjacent.time 

    			if cost < end: 
    				if cost < start: 
    					next_cost = start + time 
    				else: 
    					next_cost = cost + time
    					if start - cost + time < shortest_path[(start,machine)]:
    						pq.add({'connection':adjacent,'cost': cost+time})







graph = Graph()
m,c = [int(e) for e in raw_input().split(' ')]
start,goal = [e for e in raw_input().split(' ')]

for _m in range(m):
	graph.add_vertex(raw_input())

for _c in range(c):
	a,b,s,e,t = raw_input().split(' ')
	graph.add_edge(a,b,int(s),int(e),int(t))

answer = graph.dijkstra(start,goal)
if answer != -1 :
	print answer 
else:
	print 'TRAPPED!'

