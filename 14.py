import matplotlib.pyplot as plt
import numpy as np

x = ["python", "c", "c++", "Java"]
y = [85, 70, 60, 82]
z = [20, 30, 40, 50]

width = 0.2
p = np.arange(len(x))
p1 = [j + width for j in p]

plt.xlabel("language", fontsize=15)
plt.ylabel("No.", fontsize=15)
plt.title("wscube", fontsize=15)

plt.barh(p, y, width, color="r", label="popularity")
plt.barh(p1, z, width, color="y", label="popularity1")

plt.legend()
plt.show()
