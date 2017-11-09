B = 'B'
R = 'R'
def solve(parent,current):
	toRet = {B:0,R:0}
	if len(graph[current]) == 0: 
		if not parent or parent == B:
			toRet[B] += 1
		if not parent or parent == R:
			toRet[R] += 1 
		return toRet
	
	for node in graph[current]:
		result = solve(B,node)
		if not parent or parent == B:
			toRet[B] += result[B]
		result = solve(R,node)
		if not parent or parent == R:
			toRet[R] += result[R]

	return toRet

