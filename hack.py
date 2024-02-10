# Function to maximize the expression
def maximize_expression(a, b, c):
    max_a = max(a)
    max_b = max(b)
    max_c = max(c)

    result = (max_a ** 2 + max_b ** 2 + max_c ** 2) % 1000
    return result

# Input three lists of integers from the user
a = list(map(int, input("Enter the first list of integers: ").split()))
b = list(map(int, input("Enter the second list of integers: ").split()))
c = list(map(int, input("Enter the third list of integers: ").split()))

# Calculate and print the result
result = maximize_expression(a, b, c)
print(result)