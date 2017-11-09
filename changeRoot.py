def changeRoot(parent, newRoot):
	stack = [(newRoot,newRoot)]
	while(True):
		c_vertex,c_parent = stack[-1]
		if c_parent == parent[c_parent]:
			break
		stack.append((c_parent,parent[c_parent]))
	
	while(len(stack)):
		a,b = stack.pop()
		parent[b] = a 
	return parent

print changeRoot([0, 0, 0, 1],1)


