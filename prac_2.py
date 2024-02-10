num=4+3%9         # a%b,only when a is div by b or else a is th ans
print(num)

x=1
print(x<<2)        # The bin form of 1 is 0001. the expression x<<2 performs bitwise left shift on x.This shift gives the value 0100, which is bin value of 4 

A=[[1,2,3],[4,5,6],[7,8,9]]
print(A[1][2])              # indexing starts with zero in sublist as well 

x='abcd'
for i in range(len(x)):
    print(i)

def additem(listParam):
    listParam+=[1]
mylist=[1,2,3,4]
additem(mylist)
print(len(mylist))            