import numpy as np

def euclidean_distance(A, B):
    return np.sqrt(np.sum((np.array(A) - np.array(B)) ** 2))

def manhattan_distance(A, B):
    return np.sum(np.abs(np.array(A) - np.array(B)))

def minkowski_distance(A, B, p=3):
    return np.sum(np.abs(np.array(A) - np.array(B)) ** p) ** (1 / p)

def hamming_distance(A, B):
    if len(A) != len(B):
        raise ValueError("Inputs must be of the same length")
    return sum(a != b for a, b in zip(A, B))

# Example usage
A = [1, 2, 3]
B = [4, 5, 6]

print("Euclidean Distance:", euclidean_distance(A, B))
print("Manhattan Distance:", manhattan_distance(A, B))
print("Minkowski Distance (p=3):", minkowski_distance(A, B, p=3))
print("Hamming Distance:", hamming_distance([1, 0, 1, 1], [1, 1, 0, 1]))