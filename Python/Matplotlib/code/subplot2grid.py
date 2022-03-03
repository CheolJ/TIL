import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7))

ax1 = plt.subplot2grid((3, 3), (0, 0),
                       colspan=3,
                       fig=fig)

ax2 = plt.subplot2grid((3, 3), (1, 0),
                       colspan=2,
                       fig=fig)

ax3 = plt.subplot2grid((3, 3), (1, 2),
                       rowspan=2,
                       fig=fig)

ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.show()