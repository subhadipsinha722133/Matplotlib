import matplotlib.pyplot as plt

x = ["python", "c", "c++", "Java"]
y = [85, 70, 60, 82]
plt.xlabel("language", fontsize=15)
plt.ylabel("No.", fontsize=15)
plt.title("wscube", fontsize=15)
c = ["y", "b", "m", "g"]
plt.bar(x, y, width=0.4, color=c, edgecolor="r", label="wscube")
plt.legend()
plt.show()
