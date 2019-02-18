def oppositeSigns(x, y): 
    return ((x ^ y) < 0); 
  
x = 100
y = 1
  
if (oppositeSigns(x, y) == True): 
    print "Signs are opposite"
else: 
    print "Signs are not opposite"