# dict are used because of the limitations of list,lists are not enough to representr the real data

# example
user={'name':'saurabh','age':'19'}
print(user)
print(type(user))
   

# Accessing data, no indexing because of unordered collection of data
print(user['name'])
print(user['age'])

#eg
user_info={'name':'saurabh',
           'age':'19',
           'fav_movies':['bahubali','krrish'],
           'fav_songs':['jeena','marna']
           }
print(user_info['fav_songs'])

# Adding data to empty dictionary
user_info2={}
user_info2['name']='saurabh'
user_info2['age']='19'
user_info2['branch']='cse'
print(user_info2)

# checking if key exist
if 'name' in user_info2:
    print("Present")
else:
    print("Not present")    

# checking if value exist
if 'name' in user_info2:
    print("present")            # not for value
else:
    print("not present")  

# loop
for i in user_info2:
    print(i)          

# checking if values exist
user_info2_values=user_info2.values()
print(user_info2_values)
print(type(user_info2_values))

# item method for printing both key and value
user_items=user_info2.items()
print(user_items)
print(type(user_items))
for i,j in user_info2.items():
    print(f"key is {i} and  value is {j}")

# # popping items
popped_item=user_info2.pop('branch')              # value gets popped
print(f"popped item is {popped_item}")
print(user_info2)

# # popping both value and key
popped_item=user_info2.pop('name')                  # both key and value gets pop
print(user_info2)

# fromkeys method creates a new dictionary from given sequence of elements and values
d={'name':'unknown','age':'unknown'}
d=dict.fromkeys(['name','age'],'unknown')
print(d)

# get method
d={'name':'saurabh','age':'unknown'}
print(d['age'])

d.clear()
print(d)

 # two same keys at same time
user={'name':'Saurabh','age':'19','age':'24'}
print(user.get('fav','not found'))
print(user)