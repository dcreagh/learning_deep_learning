import numpy as np
import matplotlib.pyplot as plt

var1 = [1, 2, 3, 4, 5, 6]
var2 = [6, 5, 4, 3, 2, 1]

v1 = np.array(var1)
v2 = np.array(var2)

res1 = v1.dot(v2)
res2 = v2.dot(v1)

print (res1)
print (v1)

plt.scatter(var1, var2)
plt.plot(v2,v1)
plt.show()


