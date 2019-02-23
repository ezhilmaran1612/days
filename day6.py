def myXOR(x, y): 
    return ((x | y) &  
            (~x | ~y)) 
 
x = 3
y = 5
print("XOR is" ,  
       myXOR(x, y))