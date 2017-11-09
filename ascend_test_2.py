def shift(start,end,increment,a):
	for i in range(start,end+1):
		a[i] = chr(ord(a[i]) + increment)
	return ''.join(a)

def rollingString(s, operations):
	for operation in operations:
		i,j,ch = operation.split(' ')
		i = int(i)
		j = int(j)

		if ch == 'R':
			_s = shift(i,j,1,list(s))

		if ch == 'L':
			_s = shift(i,j,-1,list(s))
		s = _s
	return s