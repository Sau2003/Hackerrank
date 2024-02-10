# To find the greatest number among the three numbers
def greatest_nbr(a,b,c):
    if(b>a):
        a=b
    if(c>a):
        a=c
    print(a)
           
greatest_nbr(1,2,3)