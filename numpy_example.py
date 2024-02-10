
import numpy as np

my_list = [1, 2, 3, 4, 5, 6]
array = np.array(my_list, dtype=int)   # Creating array in numpy

print(array)
print(type(array))
print(len(array))
print(array.ndim)
print(array.shape)


array_2=array.reshape(3,2)  # It will modify the  array ,not changing the orignial arr
print(array_2)
array_2.shape


array_3=array.reshape(3,-1)
print(array_3)


# Inintializing numpy arrays from nested py lists
my_list2=[1,2,3,4,5]
my_list3=[2,3,4,5,6]
my_list4=[9,7,6,8,9]
mul_arr=np.array([my_list2,my_list3,my_list4])
print(mul_arr)
print(mul_arr.shape)

a=np.array([[1,2,3],[4,5,6]])
print(a.shape)

#Reshaping function to resize an array
b=a.reshape(3,2)
print(b)

# An array of evenly spaced numbers 
a=np.arange(24)
print(a)
print(a.ndim)

# Reshaping the arr a
b=a.reshape(6,4,1)

# Syntax for add
syntax=np.add(3,4)
print(syntax)

# syntrax for subtract
syntax=np.subtract(3,4)
print(syntax)

# syntax for multiply
syntax=np.multiply(2,3)
print(syntax)

# syntax for dot product
syntax=np.dot(3,4)
print(syntax)

# syntax for divide
print(1/2)
print(np.divide(3,2))

x=([1,2,3],[2,3,4])
print(np.sum(x,axis=0))   # compute sum of each column
print(np.sum(x,axis=1))   # compute sum of each row



# mean,mode,median,sd can be find by np.mean