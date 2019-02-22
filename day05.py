def turnOffK(n,k): 
   
    if (k <= 0):  
        return n 
    return (n & ~(1 << (k - 1))) 
  
n = 15
k = 4
print(turnOffK(n, k)) 