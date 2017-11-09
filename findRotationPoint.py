def findRotation(a):
	floor = 0 
	ceiling = len(a)-1

	if a[floor] < a[ceiling] : return -1 

	while True: 
		c = floor + ((ceiling - floor)/2)

		if a[c] > a[c+1]: return c + 1

		if a[floor] > a[c]: 
			ceiling = c 

		if a[floor] <= a[c]:
			floor = c 

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
print findRotation(words)
