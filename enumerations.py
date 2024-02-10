# WE USE ENUMERATE FUN  TO CHECK THE POS OF ITEM IN ITERABLE


# without using enumeration
names=['abc','sjkdnasjkdn']
pos=0
for name in names:
    print(f"{pos}:{name}")
    pos+=1

# With using enumeration
names=['anc','asdas']
for pos,name in enumerate(names):
    print(f"{pos}:{name}")

# def a fun that contains
# 1) list cont str
# 2) str that u want to find in your list and this fun will return the index of str in your lsit 
# and if str is not present print -1
names=['adsf','asddasd'] 
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1
print(find_pos(names,'adsf'))       

# Exercise: fun that takes a lsit and reverse str=true
def func(l,**kwarks):
    if kwarks.get('reverse_str')==True:
        return[name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names=['saurabh','kuche']
print(func(names,revrse_str=True))     