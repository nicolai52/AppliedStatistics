import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

times = np.load('pendul_tider/times_HLA.npy')

model =LinearRegression()

L = 22.264
x = np.arange(0, len(times)).reshape(-1, 1)

y = np.cumsum(times)
model.fit(x, y)
y_pred = model.predict(x)
residuals = y - y_pred
print(np.mean(residuals))
plt.scatter(x, residuals)
plt.axhline(0, color='red', lw=2)
plt.show()