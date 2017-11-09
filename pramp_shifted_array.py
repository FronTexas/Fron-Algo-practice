
def shifted_arr_search(a, num):
  start = 0 
  end = len(a) - 1 
  rotation = -1
  while start < end: 
    if a[start] > a[start + 1]:
      rotation = start 
      break 
    middle = start + (end - start)/2

    if a[middle] > a[end]:
      start = middle 
    else:
      end = middle
 
  if a[0] <= num and num <= a[rotation]:
    start = 0 
    end = rotation +1
  else: 
    start = rotation 
    end = len(a)

  while start < end: 
    middle = start + (end - start)/2
    
    if a[middle] == num:
      return middle

    if a[middle] < num: 
      if start == middle: 
        break
      start = middle
    else: 
      end = middle
  return -1




shiftArr = [1,2]
for num in shiftArr:
  print shifted_arr_search(shiftArr,num)
  
  

