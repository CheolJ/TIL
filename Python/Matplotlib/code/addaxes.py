import matplotlib.pyplot as plt
import numpy as np

left, bottom = 0.1, 0.1
spacing = 0.05
width1, height1 = 0.5, 0.5
width2 = 1 - (2*left + width1 + spacing)
height2 = 1 - (2*bottom + height1 + spacing)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom + height1 + spacing, 1 - 2*left, height2]
rect3 = [left + width1 + spacing, bottom, width2, height1]

fig = plt.figure(figsize=(7, 7))

ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)

plt.show()