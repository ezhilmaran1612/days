import math 
 
def maxXOR(n, k): 
    c = int(math.log(n, 2)) + 1
  
    return ((1 << c) - 1) 
  
n = 12; k = 3
print (maxXOR(n, k))