'''
    n steps 
    k steps jump
    
    n
    k 
    
    1 step or 2 step or 3 step .... k step
    [ , , , , , , , , , , x, , , ...... , , ,
    
    answers = [[....],[....]]
    

'''

'''
  n = 4 
  k = 2
  
  1 1 2 
'''
def climbingStaircaseRecursive(n,k,current_answer,level,answers):
    if level == n:
        answers.append([e for e in current_answer])
        return 
    for step in range(1,k+1):
        if level + step <= n:
            current_answer.append(step)
            climbingStaircaseRecursive(n,k,current_answer,level + step,answers)
            if len(current_answer) > 0:
                current_answer.pop()
    return

def climbingStaircase(n, k):
    answers = []
    climbingStaircaseRecursive(n,k,[],0,answers)
    return answers

def test(actual,expected):
    print 'actual = ' + str(actual)
    print 'expected = ' + str(expected)
    print actual == expected
    
n = 4 
k = 2
expected = [[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
test(climbingStaircase(n,k),expected)
