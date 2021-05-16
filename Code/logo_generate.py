from fermulerpy.analytic import *
import cmath
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

real_val = []
img_val = []
i_val = []

i = 0

while(i<=100):
    i_val.append(i)
    inp = complex(0.5,i)
    value = zeta_function(inp)
    real_val.append(value.real)
    img_val.append(value.imag)
    i = i + 1

plt.plot(real_val , img_val)
#plt.title("zeta")
plt.show()

