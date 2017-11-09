def buildLine(start,word_counter,space_counter,words):
	if word_counter == 1: 
		line = [words[start]]
		line += [' ' for s in range(space_counter)]
		return ''.join(line)

	end = start + word_counter
	line = []

	if end == len(words):
		for i in range(start,end):
			line += [words[i]]
			if space_counter > 0:
				line += [' ']
				space_counter -= 1
		while space_counter > 0: 
			line += [' ']
			space_counter -= 1 
		return ''.join(line)

	space_spots = word_counter - 1	

	if space_counter % space_spots == 0: 
		space_per_spot = space_counter / space_spots
		for i in range(start,end):
			line += [words[i]]
			if i < end-1:
				line += [' ' for s in range(space_per_spot)]
		return ''.join(line)
	else: 
		space_per_spot = space_counter / space_spots
		remainder = space_counter % space_spots

		for i in range(start,end):
			line += [words[i]]
			if i < end - 1: 
				line += [' ' for s in range(space_per_spot)]
				if remainder > 0:
					line += [' ']
					remainder -= 1
		return ''.join(line)

def textJustification(a,l):
	lengths = [len(w) for w in a]
	start = 0 
	i = start
	word_counter = 0 
	char_counter = 0 
	space_counter = 0 
	answers = []

	while start < len(a):
		while i < len(lengths) and char_counter + lengths[i] < l: 
			word_counter += 1 
			space_counter += 1
			char_counter += lengths[i] + 1 # for len of word and 1 space 
			i+=1 
		
		if i < len(lengths) and char_counter + lengths[i] == l: 
			word_counter += 1 
			char_counter += lengths[i]

		space_counter += l - char_counter
		answers.append(buildLine(start,word_counter,space_counter,a))

		start += word_counter
		i = start
		word_counter = 0 
		char_counter = 0
		space_counter = 0
	return answers



words = ["This", "is", "an", "example", "of", "text", "justification."]
l = 16
# print buildLine(0,3,8,words)
# print buildLine(3,2,7,words)
# words = ["a", "b", "c", "longword"]
# words =  ["Two", "words."]
# l = 10
# print words
ans = textJustification(words,l)
for i in range(len(ans)):
	print (ans[i] + str(len(ans[i])))


