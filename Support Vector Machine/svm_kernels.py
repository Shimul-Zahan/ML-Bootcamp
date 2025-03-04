import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# Step 1: Create a synthetic dataset
X, y = datasets.make_circles(n_samples=100, factor=0.5, noise=0.1)

# Step 2: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Step 4: SVM with Linear Kernel
svm_linear = SVC(kernel='linear')
svm_linear.fit(X_scaled, y)
ax = axes[0]
ax.set_title("Linear Kernel")
# Create a grid for visualization
xx, yy = np.meshgrid(np.linspace(X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1, 100),
                     np.linspace(X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1, 100))
Z = svm_linear.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# Plot decision boundary
ax.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.coolwarm)
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k', s=50)
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')

# Step 5: SVM with Polynomial Kernel
svm_poly = SVC(kernel='poly', degree=3)
svm_poly.fit(X_scaled, y)
ax = axes[1]
ax.set_title("Polynomial Kernel")
Z_poly = svm_poly.predict(np.c_[xx.ravel(), yy.ravel()])
Z_poly = Z_poly.reshape(xx.shape)
# Plot decision boundary
ax.contourf(xx, yy, Z_poly, alpha=0.75, cmap=plt.cm.coolwarm)
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k', s=50)
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')

# Step 6: SVM with RBF Kernel
svm_rbf = SVC(kernel='rbf', gamma=0.5)
svm_rbf.fit(X_scaled, y)
ax = axes[2]
ax.set_title("RBF Kernel")
Z_rbf = svm_rbf.predict(np.c_[xx.ravel(), yy.ravel()])
Z_rbf = Z_rbf.reshape(xx.shape)
# Plot decision boundary
ax.contourf(xx, yy, Z_rbf, alpha=0.75, cmap=plt.cm.coolwarm)
ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k', s=50)
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')

# Display the plot
plt.tight_layout()
plt.show()
