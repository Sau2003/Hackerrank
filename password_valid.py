# Check whether the password created by user is valid or not
pwd=input("Enter the password")
pwd.strip()
if (len(pwd)>=8 and len(pwd)<=16):
    print("The password length is okay")
    for p in pwd:
        if p.isupper():
            print(p,"is a uppercase letter")
        if p.islower():
            print(p,"is a lowercase letter")
        if p.isdigit():
            print(p, "is a digit") 
        if not p.isalpha() and not p.isdigit():
            print(p,"is a special char")
else:
    print("passwrod lenght must be between 8 to 10 characters")                      
