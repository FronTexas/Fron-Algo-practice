def reverse(message,begin,end):
	left = begin
	right = end - 1 

	while left < right: 
		message[left],message[right] = message[right],message[left]
		left += 1 
		right -= 1


def reverseSentence(message):
	message = list(message)
	reverse(message,0,len(message))
	index_of_last_space = 0

	for i in range(0,len(message)):
		if message[i] == ' ':
			reverse(message,index_of_last_space,i)
			index_of_last_space = i + 1
		elif i == len(message) - 1:
			reverse(message,index_of_last_space,i + 1)
	return ''.join(message)

print reverseSentence('World Hello')