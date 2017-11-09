def isThereMovie(m,l):
	movieWatched = set()
	for e in l:
		if m-e in movieWatched:
			return True
		movieWatched.add(e)
	return False
