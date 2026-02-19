import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y = np.zeros(5)
z = np.zeros(5)

x1 = np.ones(5)
y1 = np.ones(5)
z1 = [5, 3, 6, 1, 9]
f = plt.figure()
sub = f.add_subplot(111, projection = "3d")
sub.bar3d(x, y, z, x1, y1, z1)
sub.set_xlabel("X")
sub.set_ylabel("Y")
sub.set_zlabel("Z")
plt.show()