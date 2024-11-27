import numpy as np
import matplotlib.pyplot as plt

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x = np.arange(-10.0099999999, 10.01, 0.01)
ysqr = a * x**2 + b * x + c
ylog = np.log2(x)

plt.plot(x, ysqr, color = "red")
plt.plot(x, ylog, color = "blue")
for i in range(len(x)):
    if round(ysqr[i], 1) == round(ylog[i],1):
        plt.plot(x[i], ysqr[i], color="#8F00FF", marker = "o")
plt.show()