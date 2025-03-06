#include <iostream>
#include <cuda_runtime.h>

#define N 512  // Size of the vectors

// CUDA kernel to add two vectors
__global__ void vectorAdd(int *A, int *B, int *C, int n) {
    int idx = threadIdx.x + blockIdx.x * blockDim.x;  // Unique thread index
    if (idx < n) {
        C[idx] = A[idx] + B[idx];  // Add corresponding elements
    }
}

int main() {
    int *h_A, *h_B, *h_C;  // Host pointers for input and output arrays
    int *d_A, *d_B, *d_C;  // Device pointers for input and output arrays
    int size = N * sizeof(int);  // Size of the arrays in bytes

    // Allocate memory on the host
    h_A = (int *)malloc(size);
    h_B = (int *)malloc(size);
    h_C = (int *)malloc(size);

    // Initialize vectors A and B with values
    for (int i = 0; i < N; i++) {
        h_A[i] = i;
        h_B[i] = i * 2;
    }

    // Allocate memory on the device
    cudaMalloc((void **)&d_A, size);
    cudaMalloc((void **)&d_B, size);
    cudaMalloc((void **)&d_C, size);

    // Copy data from host to device
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

    // Launch the CUDA kernel with N threads, divided into blocks
    int blockSize = 256;  // Number of threads per block
    int numBlocks = (N + blockSize - 1) / blockSize;  // Calculate number of blocks needed
    vectorAdd<<<numBlocks, blockSize>>>(d_A, d_B, d_C, N);

    // Copy result from device to host
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

    // Output the result (first 10 elements)
    std::cout << "Result of vector addition (first 10 elements):\n";
    for (int i = 0; i < 10; i++) {
        std::cout << h_C[i] << " ";
    }
    std::cout << std::endl;

    // Free memory
    free(h_A);
    free(h_B);
    free(h_C);
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}
