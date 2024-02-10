# Use of function inside a function 
def greatest_nbr(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
def new_greatest(a,b,c):
    return greatest_nbr(a,b,c)

print(new_greatest(20,3,10))    