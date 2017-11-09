def get_shortest_unique_substring(arr, str):
  vc = { char : 0 for char in arr }
  
  i = 0 
  j = 1 
  counter = 0 
  
  if j < len(str) and str[j] in vc: 
    vc[str[j]] += 1 
    if vc[str[j]] == 1: 
      counter += 1 
  
  if i < len(str) and str[i] in vc: 
    vc[str[i]] += 1 
    if vc[str[i]] == 1: 
      counter += 1 
  
  if len(str) == 1 and counter == len(arr):
    return str
    
  
  ci,cj = None,None
  while j < len(str):
    # found a valid substring
    if counter == len(arr):
      # update current answer if its a shorter substring
      if ci == None: 
        ci,cj = i,j
      elif j - i  < cj - ci : 
        ci,cj = i,j 
      prev = str[i]  
      i += 1 
      if prev in vc:
        vc[prev] -=1
        if vc[prev] == 0:
          counter -= 1
    else: 
      j += 1
      # increase the counter for this valid char
      if j < len(str) and str[j] in vc: 
        vc[str[j]] += 1 
        if vc[str[j]] == 1: 
          counter += 1 
  if ci == None:
    return ''
  return str[ci:cj+1]

arr = ['x','y','z']
str = 'xyyzyzyx'
print get_shortest_unique_substring(arr,str)

arr = ["a"]
str = 'a'
print get_shortest_unique_substring(arr,str)
      
      
      