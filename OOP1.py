class Car:
    color=None
    topspeed=None

    def get_info(self,x,y):
        self.color=x
        self.topspeed=y
        print("You have the color"+str(self.color)+"and the topspeed is "+str(self.topspeed))    

    def cal_speed(self,km,t):
        self.speed=km/t
        print("Your speed is",self.speed)    

a=Car()
a.get_info(2,3)
print(a)