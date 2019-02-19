def getModulo(n, d): 
  
    return ( n & (d-1) ) 
           
n = 6
  
d = 4 
print(n,"moduo",d,"is", 
      getModulo(n, d)) 