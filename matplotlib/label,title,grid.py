
"""import matplotlib.pyplot as plt
import numpy as np

x=([2,5,6,1,5])
y=([45,50,65,87,95])

plt.plot(x,y,color="green",marker="o",mec="black",mfc="purple",ms=10)

plt.title("mark sheet",color="red",fontsize=10,fontstyle="italic" ,fontweight="bold")

plt.xlabel("student_id",color="navy",fontsize=10,fontstyle="italic" ,fontweight="bold")

plt.ylabel("student marks",color="green",fontsize=10,fontstyle="italic" ,fontweight="bold")

plt.grid(linestyle=':',color="k",linewidth=2,)
plt.grid(axis="y",color="red")
#plt.grid(False) disable grid

plt.show()"""


import matplotlib.pyplot as plt
import numpy as np

x=np.array([2,4,6])
y=np.array([8,10,12])
plt.grid()
plt.plot(x,y,"D:")
plt.show()