import numpy as np

times = np.load('pendul_tider/times_LWN.npy')

first_top = (times[:-2] + times[1:-1] + times[2:])[::3]
middel = (times[1:-1] + times[2:] + times[3:])[1::3]
last_top = (times[2:] + times[3:] + times[4:])[::3]

