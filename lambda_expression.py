# fun foer adding
def add(a,b):
    return a+b
print(add(2,3))

# adding with lambda
add2=lambda a,b: a+b
print(add(2,3))
# multiply using lambda
multiply=lambda a,b: a*b
print(multiply(2,3))

print(add)
print(add2)
print(multiply)

# practice prob
def is_even(a):
    return a%2==0 
print(is_even(5))

# Now using lambda
even_num=lambda a: a%2==0
print(even_num(3))

# practice prob of last char
def last_char(s):
    return s[-1]
print(last_char('sauru'))

# Now using lambda expression
last_char=lambda s: s[-1]
print(last_char("sau"))

# lambda with and without if else
def func(s):
    if len(s)>5:
        return True
    else:
        return False
print(func('asjdsbbdhjasbdj'))

# Now with lambda and without if else
func=lambda s: len(s)>5
print(func('asd'))

