from numpy import sin
import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return sin(x)/x
u = 1/10000
p = int(1/u)
def main(b):
  n = 0
  for i in range(1, p):
    n += f(i*u*b)*u*b
  return n
b = np.linspace(-10,10,p)
x = b
y = f(b*u)*(main(b))
plt.plot(x, y)
plt.show()
