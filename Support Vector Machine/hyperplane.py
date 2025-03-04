import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Step 1: Generate synthetic 2D data
X = np.array([[2, 3], [3, 3], [4, 3], [1, 1], [2, 1], [3, 1]])
y = np.array([1, 1, 1, 0, 0, 0])

# Step 2: Train a linear SVM classifier (just for visualization purposes)
svm = SVC(kernel='linear')
svm.fit(X, y)

# Step 3: Plot the decision boundary (hyperplane)
# Create a mesh grid to plot the decision boundary
h = 0.02  # step size in mesh grid
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict class for every point in the mesh grid
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Step 4: Plotting the decision boundary
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.Paired)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', s=50, cmap=plt.cm.Paired)
plt.title('2D SVM Hyperplane')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
