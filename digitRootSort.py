def findDigitRoot(item):
	itemSTR = str(item)
	digitRoot = 0
	for i in itemSTR:
		digitRoot += int(i)
	return digitRoot

def digitRootSort(a):
	digitToNumbers = {}
	digits = set([])

	for item in a:
		digitRoot = findDigitRoot(item)
		print(digitRoot)
		digits.add(digitRoot)
		if digitRoot in digitToNumbers:
			digitToNumbers[digitRoot].append(item)
			digitToNumbers[digitRoot] = sorted(digitToNumbers[digitRoot])
		else:
			digitToNumbers[digitRoot] = [item]

	digits = sorted(digits)
	print(digits)
	toReturn = []
	for digit in digits:
		for number in digitToNumbers[digit]:
			toReturn.append(number)
	return toReturn
