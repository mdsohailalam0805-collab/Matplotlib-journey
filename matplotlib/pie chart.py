
import matplotlib.pyplot as plt
region=['north','south','east','west']
revenue=[15000,20000,8000,30000]

plt.title('revenue contribution by region')
plt.pie(revenue, colors=['purple','red','blue'],labels=region,autopct='%1.1f%%')

plt.show()
