import matplotlib.pyplot as plt
import numpy as np
def create_plot(ptype):
    # setting the x-axis values
    x = np.arange(-10, 10, 0.01)
     
    # setting the y-axis values
    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x**2
    elif ptype == 'cubic':
        y = x**3
    elif ptype == 'quartic':
        y = x**4
             
    return(x, y)
 
# setting a style to use
plt.style.use('fivethirtyeight')
 
# create a figure
fig = plt.figure()
 
# define subplots and their positions in figure
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)
 
# plotting points on each subplot
x, y = create_plot('linear')
plt1.plot(x, y, color ='r')
plt1.set_title('$y_1 = x$')
 
x, y = create_plot('quadratic')
plt2.plot(x, y, color ='b')
plt2.set_title('$y_2 = x^2$')
 
x, y = create_plot('cubic')
plt3.plot(x, y, color ='g')
plt3.set_title('$y_3 = x^3$')
 
x, y = create_plot('quartic')
plt4.plot(x, y, color ='k')
plt4.set_title('$y_4 = x^4$')
 
# adjusting space between subplots
fig.subplots_adjust(hspace=.5,wspace=0.5)
 
# function to show the plot
plt.show()



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
#setting a custom style to use
style.use('ggplot')
 
#create a new figure for plotting
fig = plt.figure()
 
#create a new subplot on our figure
#and set projection as 3d
ax1 = fig.add_subplot(111, projection='3d')
 
#defining x, y, z co-ordinates
x = np.random.randint(0, 10, size = 20)
y = np.random.randint(0, 10, size = 20)
z = np.random.randint(0, 10, size = 20)
 
#plotting the points on subplot
 
 
#setting labels for the axes
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')
 
function to show the plot
plt.show()




#importing required modules
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

#setting a custom style to use
style.use('ggplot')

#create a new figure for plotting
fig = plt.figure()

#create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')

#defining grid size
grid_size = 5

#create a 2D grid of random values for x, y, and z
x = np.random.randint(0, 10, size=(grid_size, grid_size))
y = np.random.randint(0, 10, size=(grid_size, grid_size))
z = np.random.randint(0, 10, size=(grid_size, grid_size))

#plotting the wireframe
ax1.plot_wireframe(x, y, z)

#setting the labels
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')

plt.show()

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
#setting a custom style to use
style.use('ggplot')
 
#create a new figure for plotting
fig = plt.figure()
 
#create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')
 
#defining x, y, z co-ordinates for bar position
x = [1,2,3,4,5,6,7,8,9,10]
y = [4,3,1,6,5,3,7,5,3,7]
z = np.zeros(10)
 
#size of bars
dx = np.ones(10)              # length along x-axis
dy = np.ones(10)              # length along y-axs
dz = [1,3,4,2,6,7,5,5,10,9]   # height of bar
 
#setting color scheme
color = []
for h in dz:
    if h > 5:
        color.append('r')
    else:
        color.append('b')
 
#plotting the bars
ax1.bar3d(x, y, z, dx, dy, dz, color = color)
 
#setting axes labels
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')
 
plt.show()



# importing required modules
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
# setting a custom style to use
style.use('ggplot')
 
# create a new figure for plotting
fig = plt.figure()
 
# create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')
 
# get points for a mesh grid
u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
 
# setting x, y, z co-ordinates
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
 
# plotting the curve
ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 1)
 
plt.show()
