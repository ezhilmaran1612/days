def countSetBits( n): 
      
    if (n == 0): 
        return 0
  
    else: 
  
        return (n & 1) + countSetBits(n >> 1) 
          
n = 9
print( countSetBits(n)) 