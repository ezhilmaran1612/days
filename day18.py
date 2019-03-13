def toggleLastMBits(n,m): 
  
    if (m == 0): 
        return n 
   
    num = (1 << m) - 1
   
    return (n ^ num) 

def largeNumWithNSetAndMUnsetBits(n,m): 
  
    num = (1 << (n + m)) - 1
    return toggleLastMBits(num, m) 
  
n = 2
m = 2
  
print(largeNumWithNSetAndMUnsetBits(n, m))