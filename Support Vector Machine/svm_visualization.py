import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# Step 1: Generate synthetic data (2D)
X, y = datasets.make_blobs(n_samples=50, centers=2, random_state=6)

# Step 2: Train the SVM classifier
svm = SVC(kernel='linear')
svm.fit(X, y)

# Step 3: Get the coefficients of the decision boundary (hyperplane)
w = svm.coef_[0]
b = svm.intercept_[0]

# Step 4: Plotting the decision boundary
# Calculate the slope and intercept of the decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))

# Decision boundary: w1*x + w2*y + b = 0 => y = (-w1*x - b) / w2
Z = (-w[0] * xx - b) / w[1]

# Step 5: Plot the results
plt.figure(figsize=(8, 6))

# Plot the decision boundary
plt.contourf(xx, yy, Z, levels=[-1, 0, 1], cmap=plt.cm.coolwarm, alpha=0.1)

# Plot the support vectors
plt.scatter(svm.support_vectors_[:, 0], svm.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k', marker='x', label='Support Vectors')

# Plot all data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, s=50, edgecolors='k', label='Data points')

# Plot the decision boundary
plt.plot([x_min, x_max], [(-w[0] * x_min - b) / w[1], (-w[0] * x_max - b) / w[1]], 'k-', label='Decision Boundary')

# Add margin lines
plt.plot([x_min, x_max], [(-w[0] * x_min - b + 1) / w[1], (-w[0] * x_max - b + 1) / w[1]], 'k--', label='Margin (Positive Class)')
plt.plot([x_min, x_max], [(-w[0] * x_min - b - 1) / w[1], (-w[0] * x_max - b - 1) / w[1]], 'k--', label='Margin (Negative Class)')

# Set labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM with Linear Kernel: Decision Boundary, Support Vectors, and Margin')

# Show legend
plt.legend()

# Show the plot
plt.show()
