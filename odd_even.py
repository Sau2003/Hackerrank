def filter_odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:          # def a fun to filter odd even nbrs in a list
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output=[odd_nums,even_nums]
    return output
num=[1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(num))            