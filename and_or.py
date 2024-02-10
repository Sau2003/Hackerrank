user_name=input('Enter your name:')
user_age=int(input('Enter your age'))        # Use of and and or operator
if user_age>=10 and(user_name[0]=='a'or user_name[0]=='A'):    # OR under and
    print("You can watch the movie")
else:
    print("you can't watch the movie")    
