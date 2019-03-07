def toggleLastMBits(n,m): 
  
    num = (1 << m) - 1
    return (n ^ num) 
  
n = 107
m = 4
print(toggleLastMBits(n, m))