import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100) 

y = (x**3+3*x**2+5*x-5)

# mengatur axis di pusat
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


plt.plot(x, y, 'g')
plt.title("bolzano method")
# show the plot
plt.show()
