import numpy as np
import matplotlib.pyplot as plt
points = np.linspace(0, 10, 100)
x = np.sin(points)
y = np.cos(points)
z = points
fig = plt.figure()
sub = fig.add_subplot(111, projection = "3d")
sub.plot(x, y, z)
sub.set_xlabel("X")
sub.set_ylabel("Y")
sub.set_zlabel("Z")
plt.show()

