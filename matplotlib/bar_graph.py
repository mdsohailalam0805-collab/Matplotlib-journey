import matplotlib.pyplot as plt
import numpy as np

students=np.array(["sohail","waseem","altamash","azad"])
marks=np.array([408,444,426,434])
#plt.bar(students,marks, color="purple",width=0.2)

#horizontally graph
plt.barh(students,marks, color="purple",height=0.4)
plt.show()
