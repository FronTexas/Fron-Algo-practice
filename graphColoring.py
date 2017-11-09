def graphColoring(graph,colors):
	for node in graph: 

		if node in node.neighbors: 
			return "Impossible to solve"

		illegalColors = set([neigbor.color for neighbor in node.neighbors])

		for color in colors: 
			if color not in illegalColors:
				node.color = color
				break

