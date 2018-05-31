'''
Further reading
http://www.matplotlib.org - The project web page for matplotlib.
https://github.com/matplotlib/matplotlib - The source code for matplotlib.
http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended!
http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.

'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

# 1. Functional method

plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
#plt.show()

# subplots
plt.subplot(1,2,1)
plt.plot(x, y, 'r--') # More on color options later
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-')
#plt.show()

# 2. Object-oriented method
  # 2.1 Manual - s[ecifying axes manually

# Creates blank canvas
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes

# Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes2')
axes1.set_ylabel('Y_label_axes2')
axes1.set_title('Axes 2 Title')
axes1.set_xlim()
# Insert Figure Axes 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')

#plt.show()

  # 2.2 - Automated. Automatically creates subplots layout

# Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

# Now use the axes object to add stuff to plot
axes[0].plot(x, y, 'r')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_title('subplots[0]')

axes[1].plot(y, x, 'r')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].set_title('subplots[1]')

#plt.show()

# Save to file
fig.savefig("c:/dev/Py/Udemy-Python For Finance/fig.png")

# Legend + 2 plots on same canvas
fig = plt.figure()

ax = fig.add_axes([0.1,0.1,0.9,0.9])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()

plt.tight_layout()
plt.show()