
def findOverlap(a,b):
	return (max(a[0],b[0]),min(a[1],b[1]))

def findRectangularIntersection(r1,r2):

	xOverlap = findOverlap((r1['x'],r1['x'] + r1['width']),(r2['x'], r2['x'] + r2['width']))
	yOverlap = findOverlap((r1['y'],r1['y'] + r1['height']),(r2['y'], r2['y'] + r2['height']))

	if xOverlap[1] - xOverlap[0] <= 0 or yOverlap[1] - yOverlap[0] <= 0: 
		return 'No Intersection '

	width = xOverlap[1] - xOverlap[0]
	height = yOverlap[1] - yOverlap[0]
	x = xOverlap[0]
	y = yOverlap[0]

	return {
		'x': x,
		'y' : y,
		'width' : width,
		'height' : height
	}

print findRectangularIntersection({'x':0,'y':5,'width':10,'height':5},{'x':5,'y':0,'width':10,'height':15})



