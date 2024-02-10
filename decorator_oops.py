def gm(fun):
    def modify():
        print("Good morning")
        fun()
        print("You atre in decorator")
    return modify
    

@gm
def hello():
    print("namaste india")

@gm
def hi():
    print("Namaste bharat")    

print(hello())    

