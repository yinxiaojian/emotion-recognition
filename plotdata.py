import numpy as np
import matplotlib.pyplot as plt
plt.xlim(0,20)
plt.ylim(0,1)
plt.ion()
y = []
i = 0
plt.plot([2,0.1])
while True:
    temp = np.random.random()
    i += 1
    y.append(temp)
    if i > 20:
        plt.xlim(i-20, i)
        plt.plot([i, i], [0, 1], 'r--')
    plt.plot(y)
    plt.pause(0.1)