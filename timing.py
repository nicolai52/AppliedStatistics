import time
import numpy as np
import random
import string
counter = 0
times = []
while True:
    start_time = time.time()
    user_input =input("Press Enter to start the timer")
    if user_input == 'q':
        break
    end_time = time.time()
    print(counter)
    counter += 1
    print(end_time - start_time)
    times.append(end_time - start_time) 
np_times = np.array(times)

np.save(f'times_{''.join([random.choice(string.ascii_uppercase) for _ in range(3)])}.npy', np_times)