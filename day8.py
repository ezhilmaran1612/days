def count(n) : 
    c = 0
    while (n != 0) : 
        c += 1
        n = n >> 1
          
    return c 

def XOR(a, b) : 
    c = min(a, b) 
    d = max(a, b) 
    
    if (count(c) < count(d)) : 
        c = c << ( count(d) - count(c) )  
      
    return (c^d) 

a = 13; b = 5
print(XOR(a, b)) 