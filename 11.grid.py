import matplotlib.pyplot as plt
from matplotlib import style

day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
temperature = [23, 34, 30, 40, 43, 23, 65, 43, 46, 62, 35, 64, 74, 78, 67]

style.use("ggplot")

# plt.plot(day, temperature, color="r", marker="o", linestyle="--")
plt.plot(day, temperature, "go:", linewidth=3, markersize=8)

plt.title("Bankura Temperature ", fontsize=17)
plt.xlabel("Day", fontsize=17)
plt.ylabel("Temperature", fontsize=17)

plt.legend(["Tem line"], loc=4)
# plt.grid(color="r", linestyle="-", linewidth=2)
plt.grid(color="r", linestyle="-.", linewidth=2)

plt.show()
