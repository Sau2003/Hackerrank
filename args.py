# make flexible fun
# *operator

def total(a,b):   
    return a+b
def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total
print(all_total(1,2,3,4,5,6,76))    

# args with normal parameter
def multiply_nums(num,*args):
    multiply=1
    for i in  args:
        multiply*=i
    return multiply
print(multiply_nums(2,3,4))     # we can treat num as not args

# args as a argument
def multiply_nums(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply
nums=(2,3,4)
print(multiply_nums(*nums))

# exercise 1
def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return 'args is not present,u didnt type anything '
    
nums=[1,2,3]
print(to_power(3,*nums))



