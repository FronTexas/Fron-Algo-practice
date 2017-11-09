'''
    arr 
    num 
    
    [1,2,3,4,5] 5 
     
    
    1,4 -> 
    
    f(current_sum,start_index,current_answer,num,answers):
        if current_sum == num: 
            answers.append([e for e in current_answer])
            return
        for i in range(start_index,len(a)):
          
    1 2 3 4 5
          
    c_a = []
    
    x x x x x . . . .  x x x x x .......
                         ^
    1 1 2 2 5 5 6 8 8
          ^
     
    1 1 2 
'''
def sumSubsetsRecursive(current_sum,start_index,current_answer,answers,a,num):
    if current_sum == num: 
        answers.append([e for e in current_answer])
        return 
    if current_sum < num:
        prev = None
        for i in range(start_index,len(a)):
            if current_sum + a[i] <= num :
                if a[i] != prev:
                    current_answer.append(a[i])
                    sumSubsetsRecursive(current_sum + a[i],i + 1,current_answer,answers,a,num)
                    if len(current_answer) > 0: 
                        prev = current_answer.pop()
            else: 
                return 
def sumSubsets(arr, num):
    answers = []
    sumSubsetsRecursive(0,0,[],answers,arr,num)
    return answers 

def test(actual,expected):
    print 'actual = ' + str(actual)
    print 'expected = ' + str(expected)
    print actual == expected 

arr = [1,2,3,4,5]
num = 5
expected = [[1,4],[2,3],[5]]
test(sumSubsets(arr,num),expected)

