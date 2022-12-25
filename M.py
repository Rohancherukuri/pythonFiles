import matplotlib.pyplot as plt
import numpy as np
X = np.array([1,2,3,4,5,6,7,8])
y = np.array([3,5,8,9,1,2,6,7])
m ,c = np.polyfit(X,y,1)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(X,y,'o',color = "purple")
plt.plot(X,m*X+c)
plt.show()
