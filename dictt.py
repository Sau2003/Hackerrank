# To append the square of even elements from the list
dict=[i for i in range(0,10)]
print(type(dict))
print(dict)
l1 = []
for i in dict:
        if i%2==0:
                l1.append(i**2)
print(l1)

# Using list comprehension
dict1={i:i**2 for i in range(0,10) if i%2==0 }
print(dict1)

