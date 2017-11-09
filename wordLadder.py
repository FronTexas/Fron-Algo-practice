import Queue 
import string
class Solution(object):
	def isNeighbor(self,e,current,visited,wordSet):
		if e in visited:
			return False
		counter = 0 
		for i in range(0,len(e)):
			counter += 1 if e[i] != current[i] else 0
			if counter > 1: return False
		wordSet.discard(e)
		return True

	def ladderLength(self, beginWord, endWord, wordList):
		q = Queue.Queue()
		visited = set([])
		wordSet = set(wordList)
		q.put((beginWord,1))

		while(q.qsize() > 0):
			current,current_height = q.get()

			current_copy = [c for c in current]
			for i in range(0,len(current_copy)):
				old = current_copy[i]
				for a in string.lowercase[:26]:
					current_copy[i] = a 
					current_copy_word = ''.join(current_copy)
					if (current_copy_word in wordSet and current_copy_word not in visited):
						if current_copy_word == endWord: 
							return current_height + 1
						q.put((current_copy_word,current_height+1))
						visited.add(current_copy_word)
				current_copy[i] = old

		return 0

sol = Solution()
print sol.ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"])	