import matplotlib.pyplot as plt
import numpy as np
from random import randint

l = []
n = 0
l2 = []
while n <20000:
    n += 1000
    l.append(n)
    l2.append(randint(1,9))


lis = np.array(l)
lis2 = np.array(l2)
plt.plot(lis, lis2)
plt.ylabel('tamanho da metrix')
plt.xlabel('numero de interações')
plt.show()


