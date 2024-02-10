# # Read input
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# # Create a list using list comprehension to generate all possible coordinates
# coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

# # Filter out coordinates where the sum is not equal to n
# filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

# # Print the filtered list in lexicographic increasing order
# print(filtered_coordinates)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new=list(set(arr))
    a=sorted(new)
    print(a[n-1])