# Take user data and create dictionary
user={}
name=input("Enter your name:")
age=input("Enter your age:")
fav_movies=input("Enter your fav movies separated by commas:").split(',')

user['name']=name
user['age']=age
user['fav_movies']=fav_movies

for key,value in user.items():
    print(f"{key}:{value}")