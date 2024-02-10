# Function to find the greatest number among the two numbers
def greatest_two(a,b):
    if a>b:
        return a
    else:
        return b
num1=input("Enter the first number")
num2=input("Enter the second number")
bigger=greatest_two(num1,num2)
print(f"{bigger} is a greater nbr")

# Function to find the greatest number among the three numbers
def greatest_three(a,b,c):
    if a>=b:
        if a>=c: 
            return a  
    elif b>=a:
        if b>=c:
            return b
    else:
        return c
num1=float('Enter the 1st nbr')
num2=float('emter the 2nd nbr')
num3=float('Enter the 3rd nbr')
bigger=greatest_three(num1,num2,num3)
print(f"{bigger} is a greatest number") 




num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)