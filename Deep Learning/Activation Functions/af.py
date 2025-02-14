import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def prelu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def elu(x, alpha=1.0):
    return np.where(x> 0, x, alpha * (np.exp(x) - 1))

def selu(x, alpha=0.01, scale=1.0507):
    return scale * elu(x, alpha)

def softmax(x):
    e_x = np.exp(x - np.max(x)) 
    return e_x / e_x.sum(axis=0, keepdims=True)


def plot_activation_function(func, x_range, name):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)
    
    plt.plot(x, y)
    plt.title(f"{name} Activation Function")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show()


plot_activation_function(sigmoid, (-10, 10), "Sigmoid")
plot_activation_function(tanh, (-10, 10), "Tanh")
plot_activation_function(relu, (-10, 10), "ReLU")
plot_activation_function(leaky_relu, (-10, 10), "Leaky ReLU")
plot_activation_function(prelu, (-10, 10), "PReLU")
plot_activation_function(elu, (-10, 10), "ELU")
plot_activation_function(selu, (-10, 10), "SELU")


x = np.array([1.0, 2.0, 3.0, 4.0])
print("Softmax Output: ", softmax(x))