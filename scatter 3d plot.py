import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
sub = fig.add_subplot(111, projection = "3d")
sub.scatter(x, y, z)
sub.set_xlabel("X")
sub.set_ylabel("Y")
sub.set_zlabel("Z")
plt.show()