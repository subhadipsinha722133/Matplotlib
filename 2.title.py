import matplotlib.pyplot as plt

day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
temperature = [23, 34, 30, 40, 43, 23, 65, 43, 46, 62, 35, 64, 74, 78, 67]

plt.plot(day, temperature)

plt.title("Bankura temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.show()
