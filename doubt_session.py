
# Find the common elements from the two lists using list comprehension 
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[12,11,9,8,7]
l3=[i for i in l1 if i in l2]
    # if i in l2:
    #     print(i)
print(l3)


# To append the square of even elements from the list
dict=[i for i in range(0,10)]
print(type(dict))
print(dict)
l1 = []
for i in dict:
        if i%2==0:
                l1.append(i**2)
print(l1)

# Using list comprehension to get both key and value 
dict1={i:i**2 for i in range(0,10) if i%2==0 }
print(dict1)

   
# Using normal method to append i**2
dict=[i for i in range(0,10)]
print(type(dict))
print(dict)
l1 = []
for i in dict:
        l1.append(i**2)
print(l1)
# Using list comprehension
dict=[i**2 for i in range(0,10) if i%2==0]
print(dict)