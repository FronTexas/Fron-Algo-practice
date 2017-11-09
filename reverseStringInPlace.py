def reverse(word):
	word = list(word)
	left_pointer = 0
	right_pointer = len(word) - 1 

	while left_pointer < right_pointer:
		word[left_pointer],word[right_pointer] = word[right_pointer],word[left_pointer]
		left_pointer += 1 
		right_pointer -= 1

	return ''.join(word)


print reverse('hello')
print reverse('abcdef')
print reverse('hell')
print reverse('hello abcdef hell')