def addOne(x) : 
      
    m = 1; 
    while(x & m): 
        x = x ^ m 
        m <<= 1
    x = x ^ m 
    return x 
  
n = 13
print addOne(n) 
  