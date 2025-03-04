
# **Support Vector Machine (SVM) - Classification**

## Overview
Support Vector Machine (SVM) is a supervised machine learning algorithm primarily used for classification tasks but can also be applied to regression. SVM works by finding a hyperplane that best divides a dataset into classes. The main idea is to maximize the margin, or the distance between the hyperplane and the nearest data point from either class, called the support vectors.

In this README, we will explain the concept of SVM in detail, followed by an example of how to train an SVM model for classification using Python and the `scikit-learn` library.

## **How SVM Works**

1. **Hyperplane:**
   - In SVM, a hyperplane is a decision boundary that separates data points of different classes.
   - In 2D, the hyperplane is simply a line that divides the dataset into two classes.
   - In higher dimensions (3D, 4D, etc.), the hyperplane is a plane or hyperplane (in the case of more than 3 dimensions).

2. **Margin:**
   - The margin is the distance between the hyperplane and the nearest data points (called support vectors) of either class.
   - SVM tries to maximize this margin to increase the model’s generalization ability.

3. **Support Vectors:**
   - Support vectors are the data points that are closest to the hyperplane.
   - These data points are crucial as they define the position and orientation of the hyperplane.

4. **Kernel Trick:**
   - When data is not linearly separable, SVM uses the kernel trick to transform the data into a higher-dimensional space where it becomes separable.
   - Popular kernels include:
     - **Linear Kernel:** Used when data is linearly separable.
     - **Polynomial Kernel:** Useful when data is not linearly separable but can be separated with a polynomial boundary.
     - **RBF (Radial Basis Function) Kernel:** The most popular kernel when the decision boundary is non-linear.

## **SVM Classification Example**

In this example, we will use the famous Iris dataset to train an SVM classifier. The dataset contains measurements of 150 iris flowers, with 3 species: Setosa, Versicolor, and Virginica. We will classify the flowers based on their features using an SVM.

### **Step-by-Step Guide to Implementing SVM**

### **Step 1: Install Required Libraries**

Make sure you have the following libraries installed:

```bash
pip install scikit-learn numpy matplotlib
```

### **Step 2: Import the Libraries**

```python
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
```

### **Step 3: Load the Dataset**

We will use the Iris dataset, which is available in the `sklearn.datasets` module.

```python
# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Labels (species of iris flower)
```

### **Step 4: Split the Dataset into Training and Testing Sets**

```python
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### **Step 5: Train the SVM Classifier**

We will use the `SVC` (Support Vector Classification) from `scikit-learn` with a linear kernel.

```python
# Initialize the SVM classifier with a linear kernel
svm = SVC(kernel='linear')

# Train the model on the training data
svm.fit(X_train, y_train)
```

### **Step 6: Make Predictions**

Now that the model is trained, we will use it to make predictions on the test dataset.

```python
# Make predictions on the test set
y_pred = svm.predict(X_test)
```

### **Step 7: Evaluate the Model**

We will evaluate the model by calculating its accuracy on the test set.

```python
# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the SVM model: {accuracy * 100:.2f}%")
```

### **Step 8: Visualizing the Decision Boundaries (Optional)**

If you are working with a 2D dataset, you can visualize the decision boundaries of the SVM classifier. This is useful for understanding how the classifier separates the different classes.

For the Iris dataset, we will consider only the first two features (sepal length and sepal width) for visualization.

```python
# Plotting decision boundaries
X_train_2d = X_train[:, :2]  # Use only the first two features (sepal length, sepal width)

# Fit the model to the 2D data
svm.fit(X_train_2d, y_train)

# Create a mesh grid for plotting
h = 0.02  # Step size for the mesh grid
x_min, x_max = X_train_2d[:, 0].min() - 1, X_train_2d[:, 0].max() + 1
y_min, y_max = X_train_2d[:, 1].min() - 1, X_train_2d[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict class for every point on the mesh grid
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary and the training points
plt.contourf(xx, yy, Z, alpha=0.75)
plt.scatter(X_train_2d[:, 0], X_train_2d[:, 1], c=y_train, edgecolors='k', marker='o', s=50, cmap=plt.cm.Paired)
plt.title("SVM Decision Boundary")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
```

### **Step 9: Tuning Hyperparameters (Optional)**

You can improve the performance of your SVM classifier by tuning the hyperparameters. For example, you can adjust the `C` parameter, which controls the trade-off between maximizing the margin and minimizing classification error. You can also experiment with different kernels like the Radial Basis Function (RBF) kernel.

```python
# SVM with RBF kernel
svm_rbf = SVC(kernel='rbf', C=1, gamma='scale')
svm_rbf.fit(X_train, y_train)
```

### **Conclusion**

In this guide, we've learned how to implement and train a Support Vector Machine (SVM) classifier using Python. We used the Iris dataset for classification and visualized the decision boundary for the 2D case. SVM is a powerful algorithm for both linear and non-linear classification problems, and with the kernel trick, it can handle more complex datasets.

### **Key Points**
- **Hyperplane**: The decision boundary that separates classes.
- **Support Vectors**: The points that define the margin and the hyperplane.
- **Kernel Trick**: A technique to map non-linearly separable data to a higher-dimensional space.
- **SVM Types**: Different types of kernels like Linear, Polynomial, and RBF can be used based on the problem.

