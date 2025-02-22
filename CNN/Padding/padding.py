import numpy as np

# Input Matrix (3×3)
input_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Filter (Kernel) (2×2)
kernel = np.array([
    [1, 0],
    [0, -1]
])

# Padding
padding = 1
input_padded = np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0)

# Get dimensions
input_size = input_matrix.shape[0]
kernel_size = kernel.shape[0]
output_size = input_size  # Since we're using 'same' padding

# Output Feature Map (Initialized to zeros)
output = np.zeros((output_size, output_size))

# Convolution Operation
for i in range(output_size):
    for j in range(output_size):
        # Element-wise multiplication and sum
        output[i, j] = np.sum(
            input_padded[i:i+kernel_size, j:j+kernel_size] * kernel
        )

print("Padded Input:")
print(input_padded)
print("\nOutput Feature Map:")
print(output)
