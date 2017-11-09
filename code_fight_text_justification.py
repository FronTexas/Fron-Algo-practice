
import math 

def buildLine(words_container,spaces):
    theLine = ''
    for i,w in enumerate(words_container): 
        theLine += w
        if i < len(spaces): 
            for space in range(spaces[i]):
                theLine += ' '
    return theLine

def buildSpaces(num_space,num_words):
    spaces = []
    if num_words - 1 == 0:
        space_between = num_space
    else:
        space_between = int(math.ceil(float(num_space) / float(num_words - 1)))
    while num_space > 0: 
        if num_space - space_between >= 0: 
            spaces.append(space_between)
        else: 
            spaces.append(num_space)
        num_space -= space_between
    return spaces

'''
words = [w1 w2 w3 .... wk .... wn]

current_line_counters = len(w1) + s + len(w2) + .... until the sum of current_line == 16 

if current_line_counters> 16 -> remove last word and replace it with space?



    [         ] -> num_of_char + num_of_space

    [         ]
    [         ]
    .
    .
    .

words =        [w1 w2 w3 ....wj wk wl wm .... wn]
                                ^
words_length = [n1 n2 ....   nj nk nl nm...  nn]

current_line_counters = [n1,1]

words_container = []

answers = []

    
'''

def textJustificationRecursive(i_words,words,words_length,l,current_line_counters,words_container,answers,done):
    num_char , num_space = current_line_counters
    # Base Case
    if num_char + num_space == l: 
        spaces = buildSpaces(num_space,len(words_container))
        theLine = buildLine(words_container,spaces)
        answers.append(theLine)
        if i_words == len(words):
            done[0] = True
        return 
    # Base Case End

    if i_words == len(words):
        return 
    
    _num_char = num_char
    _num_space = num_space 

    _num_char += words_length[i_words]

    if _num_char + _num_space > l: 
        return 
    else: 
        words_container.append(words[i_words])
    while _num_char + _num_space <= l: 
        if not done[0]:
            textJustificationRecursive(i_words + 1,words,words_length,l,(_num_char,_num_space + 1),words_container,answers,done)
        _num_space += 1
    current_line_counters = (0,0)
    words_container = []
    if not done[0]:
        textJustificationRecursive(i_words + 1,words,words_length,l,current_line_counters,words_container,answers,done)

def textJustification(words, l):
    words_length = [len(w) for w in words]
    answers = []
    textJustificationRecursive(0,words,words_length,l,(0,0),[],answers,[False])
    return answers

words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["Two", "words."]
l = 11

print textJustification(words,l)

# print buildSpaces(5,1)


# words_container = ['This','Is','An']
# spaces = [4,4]
# print buildSpaces(8,3)
# print buildLine(words_container,spaces)

# spaces = buildSpaces(5,3)
# print buildLine(words_container,spaces)
    


    
    
