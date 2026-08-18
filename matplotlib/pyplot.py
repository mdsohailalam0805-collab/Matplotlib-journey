
#draw a line
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,4,6])
y=np.array([8,10,12])
plt.plot(x,y)
plt.xlabel("days")
plt.ylabel("sales")
plt.grid()
plt.show()

#draw without line
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,4,6])
y=np.array([8,10,12])
plt.plot(x,y,marker="o",lw="3",mec="black",color="yellow")
plt.title("simple graph")
x1=np.array([5,1,5])
y1=np.array([6,4,8])
plt.plot(x1,y1,marker="o",lw="2",ms=5,mec="blue",color="purple")
plt.show()
