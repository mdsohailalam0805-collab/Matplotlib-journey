import matplotlib.pyplot as plt
import numpy as  np

x=np.array([2,4,6,7])
y=np.array([3,5,9,8])
plt.subplot(3,1,1)
plt.plot(x,y)
plt.title("1st graph")


x=np.array([2,4,2,3])
y=np.array([3,3,7,8])
plt.subplot(3,1,2)
plt.plot(x,y)
plt.title("2nd graph")


x=np.array([1,4,2,3])
y=np.array([3,1,2,4])
plt.subplot(3,1,3)
plt.plot(x,y)
plt.title("3rd graph")


x=np.array([2,1,3,1])
y=np.array([3,5,5,4])
plt.subplot(3,1,3)
plt.plot(x,y)
plt.title("4th graph")


x=np.array([2,4,2,3])
y=np.array([3,3,3,3])
plt.subplot(3,1,3)
plt.plot(x,y)
plt.title("5th graph")

plt.show()
