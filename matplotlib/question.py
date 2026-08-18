import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]
sales = [20000, 25000, 30000, 22000, 35000, 40000]

plt.bar(months, sales)

plt.title("Monthly Sales of a Shop")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.xticks(rotation=45)
plt.show()