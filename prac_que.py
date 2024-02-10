# # # list=[1,9,8,5,7,4,3]     # program to multiply 3 largest nbr of list
# # # list.sort()
# # # print(list)
# # # print(max(list))
# # # print(list[-2])
# # # print(list[-3])
# # # print(list[-2]*list[-3]*max(list))

# # # def mult(list):         # fun to do the same 
# # #     list.sort()
# # #     print(max(list))
# # #     print(list[-2])
# # #     print(list[-3])
# # #     print(max(list)*list[-2]*list[-3])
# # # list=[1,4,3,5,6,8,7,9]
# # # print(mult(list))    


# # # # Creating 3 functions
# # # # 1. Return the highest score
# # # # 2. Return the lowest score
# # # # 3. Return the list in the sorted manner

# # # students = [('Magnus', 85), ('Max', 90), ('Charlie', 80), ('Raven', 75), ('Silver', 70), ('Alice', 95)]
# # # # name, highestScore = students[0]

# # # def highest_score(students):
# # #   topperName, topScore = students[0]
# # #   for student in students:
# # #     name, score = student
# # #     if score > topScore:
# # #       topperName = name
# # #       topScore = score
  
# # #   return (topperName, topScore )

# # # topper = highest_score(students)
# # # print(topper)

# # # # With lambda function

# # # def lowestScore(students):
# # #   sortedList = sorted(students, key=lambda student: student[1])
# # #   return sortedList[0]

# # # lowest = lowestScore(students)
# # # print(lowest)
 


# # # # Given a string, you have to determine the alphabets that are present in it.
# # # # Also if possible, try to identify which vowels are present as well

# # # def find_alphabets_and_vowels(string):
# # #     alphabets =set()
# # #     vowels = set()
# # #     string = string.upper()
    
   
# # #     for char in string:
# # #         if char.isalpha():
# # #             alphabets.add(char)
# # #             if char in 'AEIOU':
# # #                 vowels.add(char)
  
   
    
# # #     return alphabets , vowels
  
# # # string = "JSPM colleges are committed to provide value based quality education"
# # # print(find_alphabets_and_vowels(string))


# # # def freq_str(string):
# # #   string = string.lower()
# # #   freq={}
# # #   for char in string:
# # #     if char not in freq:
# # #       freq[char] = 1
# # #     else:
# # #       freq[char] += 1 
# # #   return freq
# # # # freq = { 'a': 4, 'i': 9, 'e': 10}

# # # string = "JSPM colleges are committed to provide value based quality education"
# # # print(freq_str(string))    


# # # # Find the distance between two given points

# # # x1=int(input('Enter x1'))        # without using func
# # # x2=int(input('Enter x2'))
# # # y1=int(input('Enter y1'))
# # # y2=int(input('Enter y2'))
# # # a=x2-x1
# # # b=y2-y1
# # # print(a**2 +b**2)**0.5

# # # def dist_points(x1,x2,y1,y2):        # using func  
# # #     a=x2-x1
# # #     b=y2-y1

# # #     return (a**2 + b**2)**0.5
# # # print(dist_points(2,1,2,1))


# # # You have the dataset of the list of friends of 3 users.
# # # You have to determine which all people are friends of all the 3 users.
# # # You also have to find the non-common friends

# # Alice_friends = {'Alice','Magnus', 'Max', 'Charlie', 'Agatha', 'Bob'}
# # Bob_friends = {'Bob','Violet', 'Collei', 'Magnus', 'Charlie', 'Alice'}
# # Charlie_friends ={'Charlie','Alice', 'Bob', 'Violet', 'Agatha', 'Magnus'}
# # f1=Alice_friends
# # f2=Bob_friends
# # f3=Charlie_friends
# # common_friends=f1&f2&f3         # common friends by intersection method 
# # non_common_friends=(f1 | f2 | f3)-common_friends   # non common friends
# # print("Common friends",common_friends)
# # print("Non common friends",non_common_friends)

# # Q))) Sorting items in a list based upon a certain attribute

# # Sort by Profit earned in each item
# # Sort by Quantity
# # Give the costliest item in the itemset
# # Give the cheapest item in the itemset
# # Give the item that gives the most profit
# # Give the item that gives the least profit
# items = [
#   # ("Item_name", CP, SP, Quantity)
#     ("Blue ink pens", 16, 20, 286 ),
#     ("Black ink pens", 18, 20, 726),
#     ("100 Page books", 25, 30, 678),
#     ("500 Page books", 65, 80, 814),
#     ("Erasers", 3, 6, 369),
#     ("Pencils", 6, 10, 312)
# ]


# sorted_items_by_profit = sorted(items, key=lambda i: i[2] - i[1])
# print("Sorted by profit")
# print(sorted_items_by_profit)
# print()
# sorted_items_by_quantity = sorted(items, key=lambda i: i[3])
# print("Sorted by quantity")
# print(sorted_items_by_quantity)
# print()
# costliest_item = max(items, key=lambda i: i[2])
# print("costlist item is")
# print(costliest_item)
# print()
# cheapest_item = min(items, key=lambda i: i[2])
# print("Cheapest item is")
# print(cheapest_item)
# print()
# most_profitable_item = max(items, key=lambda i: i[2] - i[1])
# print("Most profatable is")
# print(most_profitable_item)
# print()
# least_profitable_item = min(items, key=lambda i: i[2] - i[1])
# print("least profitable is")
# print(least_profitable_item)
# print()

fac=lambda num: 1 if num==0 else num*fac(num-1)
print(fac(5))






