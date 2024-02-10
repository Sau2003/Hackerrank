from itertools import permutations

# Read input from STDIN
input_str=input()
length = input()
length = int(length)

# Generate permutations of the specified length from the input string
pr = list(permutations(input_str, length))

# Sort the permutations lexicographically
pr.sort()

# Print each permutation separately
for perm in pr:
    print("".join(perm))
