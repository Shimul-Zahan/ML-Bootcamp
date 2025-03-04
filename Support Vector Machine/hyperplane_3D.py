from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Step 1: Generate synthetic 3D data
X = np.array([[1, 2, 3], [2, 3, 4], [3, 3, 5], [3, 4, 6], [4, 4, 7], [1, 1, 1]])
y = np.array([0, 0, 0, 1, 1, 1])

# Step 2: Train a linear SVM classifier (just for visualization purposes)
svm = SVC(kernel='linear')
svm.fit(X, y)

# Step 3: Create mesh grid for 3D plot
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
z_min, z_max = X[:, 2].min() - 1, X[:, 2].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))
zz = (-svm.coef_[0][0] * xx - svm.coef_[0][1] * yy - svm.intercept_) / svm.coef_[0][2]

# Step 4: Plotting the 3D decision surface (hyperplane)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the decision surface
ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)

# Plot the data points
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, s=50, cmap=plt.cm.Paired)
ax.set_title('3D SVM Hyperplane')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
plt.show()
