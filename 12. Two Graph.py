import matplotlib.pyplot as plt
from matplotlib import style

day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
bankura_temperature = [23, 34, 30, 40, 43, 23, 65, 43, 46, 62, 35, 64, 74, 78, 67]
durgapur_temperature = [2.3, 84, 30, 4.0, 43, 23, 6.5, 30, 27, 20, 50, 66, 70, 48, 77]

style.use("ggplot")

plt.plot(
    day,
    durgapur_temperature,
    color="r",
    marker="o",
    linestyle="--",
    label="Bankura_Tem",
)
plt.plot(
    day, bankura_temperature, "go:", linewidth=3, markersize=8, label="Durgapur_Tem"
)

plt.title("Bankura & Durgapur Temperature ", fontsize=17)
plt.xlabel("Day", fontsize=17)
plt.ylabel("Temperature", fontsize=17)

plt.legend(loc=4)
# plt.grid(color="r", linestyle="-", linewidth=2)
plt.grid(color="y", linestyle="-.", linewidth=2)

plt.show()
