# MEAN
list=[1,2,3,4,5,6,7,8,9,10]

a=len(list)  # Lenght of list is the number of the obs
print(f"The number of obs are{a}")
summation=0
for i in range(0,a):
    summation+=list[i]
print(f"The summation of the gievn nbrs is {summation}")

Mean=summation/a
print(f"The mean of the given data is {Mean}")

# MODE
number_list = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8]
a = []
b = []
for i in number_list:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
print(max(b))

# # MEDIAN
# list of elements to calculate median
n_num = [1,2,3,4,5,6]
n = len(n_num)
n_num.sort()
 
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print(f"Median is:{median}")




# Variance and Standard deviation
import math
list=[10,20,30,40,50]
mean=sum(list)/len(list)
print(mean)
new=[(list[x]-mean)**2 for x in range(0,len(list))]
print(new)
count=0
for i in range(0,len(list)):
    count+=new[i]
print(count)    
variance=count/len(list)-1   
print(variance)
c=math.sqrt(variance)
print("The SD is ",c)

