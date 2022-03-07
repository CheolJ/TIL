import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 13))

axes_g1 = np.empty(shape=(0,))
main = plt.subplot2grid((5,4), (0,0), 2, 2, fig=fig)

axes_g1 = np.append(axes_g1, main)
for r_idx in range(2, 2 + 3):
    for c_idx in range(2):
        ax = plt.subplot2grid((5,4), (r_idx, c_idx), fig=fig)
        axes_g1 = np.append(axes_g1, ax)

axes_g1 = axes_g1.reshape(1,-1)
print(axes_g1.shape)
