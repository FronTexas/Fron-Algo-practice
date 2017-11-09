from math import log10, floor
def round_sig(x, sig=2):
  return round(x, sig-int(floor(log10(abs(x))))-1)

def root(x, n):
  lower = float(0) 
  upper = float(x) 
  
  while(lower<=upper):
    mid = lower + float((upper-lower)/2)
    if(abs(mid**n - x) < 0.001):
      return round_sig(mid,4)
    
    if(mid**n < x):
      lower = mid
    else:
      upper = mid
  return 0 

print root(7,3)
print root(9,2)
print root(160,3)