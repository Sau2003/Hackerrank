 
from tkinter import *
#Initialize Window
root =Tk()
root.geometry("400x550") #size of the window by default
root.resizable(0,0)#to make the window size fixed
#title of our window
root.title("Weather forecast Application")
#Frontend part of code - Interface
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading

inp_city = Entry(root,   width = 24, font='Arial 14 bold').pack() 
#to generate label for weather 
Label(root, text = "Check Weather", font="Roman", bg='black', fg='white', activebackground="red", padx=5, pady=5 ).pack(pady= 15) 
# temp button  in celcius,kelvin, and farenheit 
celcius=Button(root, text = "In celcius", font="Arial 10", bg='lightblue', fg='black', activebackground="red", padx=5, pady=5 )
celcius.pack(pady= 8) 
kelvin=Button(root, text = "In kelvin", font="Arial 10", bg='lightblue', fg='black', activebackground="red", padx=5, pady=5 )
kelvin.pack(pady= 8)
farenheit=Button(root, text = "In farenheit", font="Arial 10", bg='lightblue', fg='black', activebackground="red", padx=5, pady=5 )
farenheit.pack(pady= 8)
#to show output
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold')
weather_now.pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack() 
#to show next 6 days foecast 

prediction=Button(root, text = "next 6 days ", font="Arial 10", bg='lightblue', fg='black', activebackground="green")
prediction.place(x=50,y=500) 
graph=Button(root, text = "Graph", font="Arial 10", bg='lightblue', fg='black', activebackground="green")
graph.place(x=300,y=500) 
root.mainloop()


