# To find letter is present in string or not
name="saurabh"
if 's' in name:
    print("s is present in name")
else:
    print("not present")   


# To check whether empty or not  = use if else 
name=input("Enter your name")
if name:
    print(f"Your name is {name}")
else:
    print("You didnt type anything")



# To find the sum of nbrs using while loop
total=0
i=1
while i<=10:
    total=total+i
    i+=1
print(total)



# To find the sum of digits in a number by using while loop
number=input("Enter the number")
total=0
i=0
while i<len(number):
    total=total+int(number[i])
    i=i+1
print(total)   



#  To find count of each letter  in a name
name=input("Enter your name")
i=0
while i<len(name):
    print(f"{name[i]}: {name.count(name[i])}")
    i+=1

    

# To find count of each words in a name by using temp 
name=input("enter your name")
temp_var=""
i=0
while i<len(name):
    if name[i] not in temp_var:
        temp_var+=str(i)
        print(f"{name[i]}:{name.count(name[i])}")
        i+=1    