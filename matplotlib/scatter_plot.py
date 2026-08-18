
import matplotlib.pyplot as plt
import numpy as np

x=([15,17,18,20,22])
y=([45,51,54,60,66])

colors=(['red','blue','black','purple','green'])

sizes=([5,10,15,20,25])

plt.scatter(x,y ,c=colors,marker="*",s=sizes,cmap="hot")

plt.title("Graph")
plt.colorbar()
plt.show()