numbers=list(range(1,11))
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)        


# Now using list comprehension
even_list=[i for i in numbers if i%2==0]
print(even_list)
odd_list=[i for i in numbers if i%2!=0]
print(odd_list)

# num to str using list comprehension
def num_str(l):
    return[str(i) for i in l if (type(i)==int or type(i)==float)]
print(num_str([True,False,[1,2,3],1,1.2,3]))