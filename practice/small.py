
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Line Plot")
plt.show()



import matplotlib.pyplot as plt

movies = ["A", "B", "C", "D"]
ratings = [8, 6, 9, 7]

plt.bar(movies, ratings)
plt.xlabel("Movies")
plt.ylabel("Rating")
plt.title("Movie Ratings")
plt.show()