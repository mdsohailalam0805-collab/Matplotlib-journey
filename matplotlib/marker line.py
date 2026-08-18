import matplotlib.pyplot as plt
import numpy as np
x=[20,3,9,15]
y=[15,16,8,13]

plt.plot(x,y,marker="o")

plt.plot(x,y, marker="o",color="red")# line color red color="red"

plt.plot(x,y,marker="o",color="red",ms=10) #markersize ms=10

plt.plot(x,y,marker="o",color="red",ms=10,markerfacecolor="yellow") # inside color

plt.plot(x,y,marker="o",color="red",ms=10,markerfacecolor="yellow",markeredgecolor="black") # border color

plt.plot(x,y,marker="o",color="red",ms=10,markerfacecolor="yellow",markeredgecolor="black",linestyle="-.",linewidth=3) #line style

#we can combine marker + line style
plt.plot(x,y,"o--") #marker with dashed line

plt.show()