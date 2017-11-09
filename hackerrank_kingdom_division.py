# https://www.hackerrank.com/challenges/kingdom-division

'''
	At each node, there are bunch of possibilities; 
		(1) You are a leaf node 
			(1) You need to follow parent's color
		(2) You are inner node
			(1) You have siblings that are the same with your parent
				(1) Freedom
			(2) You don't
				(1) Follow parent

		   (B)
          /
 		(B)
	   /   \
	 (R)    (R)
	/  \    /  \
   (R)  (R)(R)  (R)

   		  (B)-()
          /
 		(B) <----- Root
	   /   \
	 (B)    (B)
	/  \  /  \
   (B)  (B)(B)  (B)


   		  (B)-(R)
          /
 		(B) <----- Root
	   /   \
	 (R)    (R)
	/  \  /  \
   ()  ()()  ()

      	   (R)-()
          /
 		(B) <----- Root
	   /   \
	 ()    ()
	/  \  /  \
   ()  ()()  ()


'''
def buildGraph(n):
	graph = {}
	for _n in range(n-1):
		a,b = [int(e) for e in raw_input().strip().split(' ')]
		if a in graph:
			graph[a].append(b)
		else: 
			graph[a] = [b] 

		if b in graph:
			graph[b].append(a)
		else: 
			graph[b] = [a] 
	return graph

def findLeafNodes(graph):
	leafs = []
	for key in graph:
		value = graph[key]
		if len(value) == 1:
			leafs.append(key)
	return leafs

def solve(leaf_nodes,graph):
	current_level_nodes = leaf_nodes
	visited = set(leaf_nodes)
	answer = 1
	dp = []
	while len(current_level_nodes) > 0:	
		next_level_nodes = []
		for node in current_level_nodes: 
			for child in graph[node]:
				if child not in visited:
					next_level_nodes.append(child)
					visited.add(child)
		print 'next_level_nodes = ' + str(next_level_nodes)
		answer *= 2**len(next_level_nodes)
		print 'answer = ' + str(answer)
		dp.append(2**len(next_level_nodes))
		if len(next_level_nodes) == 1: 
			if len(dp) - 2 > 0:
				print 'sub dp = ' + str(dp[0:len(dp)-2])
				print 'reduce = ' + str(reduce(lambda x,y: x*y,dp[0:dp[len(dp)-2]]))
				answer -= reduce(lambda x,y: x*y,dp[0:len(dp)-2]) * 2
			else:
				answer -= 2
		current_level_nodes = next_level_nodes
	print dp
	return answer

n = int(raw_input())
graph = buildGraph(n)
leaf_nodes = findLeafNodes(graph)
print 'leaf_nodes = ' + str(leaf_nodes)
print solve(leaf_nodes,graph)
