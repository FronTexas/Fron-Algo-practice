def flip(a,k):
  start = 0 
  end = k 
  while start < end: 
    a[start],a[end] = a[end],a[start]
    start += 1 
    end-=1 
  
def findMaxIndex(arr,end):
  _max = arr[0]
  _max_index = 0
  for i in range(end + 1):
    if arr[i] > _max:
      _max_index = i 
      _max = arr[i]
  return _max_index
  
def pancake_sort(arr):
  end = len(arr) - 1
  while end > 0:
    max_index = findMaxIndex(arr,end)
    flip(arr,max_index)
    flip(arr,end)
    end -= 1
  return arr

print pancake_sort([1,5,4,3,2])
