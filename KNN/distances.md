# Distance Metrics Implementation

## Overview

This project implements several common distance measurement techniques used in k-Nearest Neighbors (k-NN) and other machine learning applications:

- **Euclidean Distance (ED)** - Measures the straight-line distance between two points.
- **Manhattan Distance (MD)** - Measures the sum of absolute differences.
- **Minkowski Distance (MinikD)** - Generalized distance metric (includes Euclidean and Manhattan as special cases).
- **Hamming Distance (HD)** - Measures the number of positions at which two binary sequences differ.
- **Chebyshev Distance** - Measures the maximum absolute difference between coordinates.
- **Cosine Similarity** - Measures the cosine of the angle between two non-zero vectors.
- **Mahalanobis Distance** - Considers feature correlations for more accurate distance measurement in high-dimensional data.

## Real-Life Examples

### 1. Euclidean Distance (ED)
**Example:** Measuring the straight-line distance between two cities on a map.  
**Use Case:** GPS navigation systems use Euclidean distance to calculate the shortest path between two points.

### 2. Manhattan Distance (MD)
**Example:** Walking through a city with only right-angle turns (like New York streets).  
**Use Case:** Used in taxi fare calculations where movement is restricted to a grid-like path.

### 3. Minkowski Distance (MinikD)
**Example:** A generalization of both Euclidean and Manhattan distances.  
**Use Case:** Used in ML models where the distance metric needs flexibility based on the dataset.

### 4. Hamming Distance (HD)
**Example:** Comparing two DNA sequences to find mutations.  
**Use Case:** Used in error detection and correction in digital communication.

### 5. Chebyshev Distance
**Example:** The maximum number of moves a king needs to move between two squares in chess.  
**Use Case:** Used in warehouse logistics where movement is constrained in multiple directions.

### 6. Cosine Similarity
**Example:** Comparing two text documents to check for plagiarism.  
**Use Case:** Used in search engines to rank similar documents based on keyword distribution.

### 7. Mahalanobis Distance
**Example:** Finding anomalies in a dataset based on correlated features.  
**Use Case:** Used in fraud detection to identify unusual transactions.

## Usage

This implementation is written in Python and uses **NumPy** for efficient calculations.
