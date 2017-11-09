# Enter your code here. Read input from STDIN. Print output to STDOUT

Z = ord('z')
A = ord('a')

def compute_cyclical(x,lower,upper):
    if lower <= x <= upper: 
        return chr(x)
    return chr(((x % upper)) % (upper - lower + 1) + lower - 1)

def _compute_cyclical(x):
    if A <= x <= Z: 
        return chr(x)
    return chr(((x % Z)) % (Z - A + 1) + A - 1)


def _solution(s):
    counter_dict = {chr(i) : 0 for i in range(ord('a'),ord('z') + 1)}
    output = []
    for c in s: 
        output.append(_compute_cyclical(ord(c) + counter_dict[c]))
        counter_dict[c] += 1
    return ''.join(output)

def solution(s,k):
    output = []
    for c in s: 
        if ord('a') <= ord(c) <= ord('z'):
            output.append(compute_cyclical(ord(c) + k,ord('a'),ord('z')))
        elif ord('A') <= ord(c) <= ord('Z'):
            output.append(compute_cyclical(ord(c) + k,ord('A'),ord('Z')))
        else:
            output.append(c)
            
    return ''.join(output)

print _solution('zzzzzzzzz')
print solution('159357lcfd',98)







