# Denoising and pattern recognition

# Library
import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

## Varoables
path = './Signal Processing/data/raw_data_0304_160Mbps_5sec.cap0'

################################################################
#####              Data Pre-processing Part                 ####
################################################################


raw_signal = np.fromfile(path, dtype='int16')



fig, axes = plt.subplots(3, 1, figsize=(12, 9))