print("Hello world")

# addn of two nbrs
num1=int(input("Enter the first nbr: "))
num2=int(input("Enter the second nbr: "))
sum=num1+num2
print(sum)

# string as input and lenght as output
name=input("Enter your name: ")
length=len(name)
print(length)

# list of nbr as input and output their sum
num_list=input("Enter a list of nbrs seperated by spaces: ").split()
num_list=[int(num) for num in num_list]
sum=sum(num_list)
print(f"the sum of nbrs present in list is {sum}")

# list of strings as input and output the lenght of longest string
list_string=input("Enter the strings separated by spaces: ").split()
length=[len(string) for string in list_string]
longest_length=max(length)
print(f"The length of  longest string is {longest_length}")

# list of int as input and output the largest int
num_int=input("Enter the intergers separated by spaces").split()
num_int=[int(num) for num in num_int]
largest_int=max(num_int)
print(f"The largest integer is {largest_int}")

# string as input and reverse as input
name=input("Enter your name: ")
rev_name=name[::-1]
print(f"YOur name in reverse order is {rev_name}")
 
# input as a list and output as a new list with strings in alphabetical order
list=input("Enter the strings separated by space: ").split()
list.sort()
print(list)

# list of integer as input and output a new list with int sorted in descending order
list=input("Enter the numbers separated by space: ").split()
list=[int(num)for num in list]
list.sort(reverse=True)
print(list)

# input as two str and output as a concentrated str
str1=input("Enter the 1st string: ")
str2=input("Enter the 2nd string: ")
str3=str1+str2
print(f"The concentrated string is {str3}")

# input a string and output nbr of vowels in the str
str=input("Enter the string: ")
vowels='aeiouAEIOU'
count=0
for char in str:
    if char in vowels:
        count+=1
print(f"The nbr of vowels in string is {count}")        

# input as list of int and output sum of even int in list
num_list=input("Enter the numbers separated by spaces: ").split()
num_list=[int(num) for num in num_list]
even_num=[num for num in num_list if num%2==0]
sum_even=sum(even_num)
print(f"The sum of even numbers in list is: {sum_even}")

