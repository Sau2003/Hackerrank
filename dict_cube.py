# Define a function that takes a nbr n and return a dict cube of nbrs from 1 to n
def cube_finder():
    cubes={}
    for i in range (1,n+1):
        cubes[i]=i**3
    return cubes
n=4
print(cube_finder())    