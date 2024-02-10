#Adding data to list
fruits=['grapes','mango']
fruits.append('banana')
print(fruits)

# to concentrate two strings
fruits1=['mango','banana']
fruits2=['grapes','oranges']
fruits=fruits1+fruits2
print(fruits)

# extend method
fruits1=['mango','oranges']
fruits2=['apple','banana']
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

# pop method to del
fruits=['mango','orange','banana']
fruits.pop(0)            # MENTION THE INDEX
print(fruits)

# rem method to del
fruits=['mango','orange','banana']
del fruits[1]             # MENTION THE INDEX

#rem meth 
fruits=['mango','orange','banana']
fruits.remove('mango')
print(fruits)

# To check in list
fruits=['mango','orange','banana']
if 'mango' in fruits:
    print("present")
else:
    print("not present")    

# count method
fruits=['mango','orange','banana','orange']
print(fruits.count('orange'))

# sort method
fruits=['mango','orange','banana','orange']
fruits.sort()
print(fruits)

# clear method
fruits=['mango','orange','banana','orange']
fruits.clear()
print(fruits)

# copy method
fruits=['mango','orange','banana','orange']
fruits.copy()
print(fruits)

# string into list conversion
name,age=input("Enter your name and age").split(',')
print(name)
print(age)

# list into string conversion by join method
user_info=['saurabh','19']
print(',' .join(user_info))

# loops in lists
fruits=['orange','grapes','mango']
for fruit in fruits:
    print(fruit)

# list under list
matrix=[[1,2,3],[4,5,6]]
for sublist in matrix:
    for i in sublist:
        print(i)
print(type(matrix))    

# popping items
numbers=['1','2','3','5']
popped_item=numbers.pop(1) 
print(numbers) 
print(numbers.index())




list=[1,2,3,4,5]
for num in list:
    print(num**2  if num==list[-1] else num)
    


