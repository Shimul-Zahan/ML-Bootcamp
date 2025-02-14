md_content = """
# Activation Functions in Neural Networks

Here's a comprehensive table summarizing different activation functions, their formulas, usage, advantages, and disadvantages:

| **Activation Function** | **Formula** | **Range** | **Usage** | **Advantages** | **Disadvantages** |
|-------------------------|-------------|-----------|-----------|----------------|-------------------|
| **Sigmoid** | \(\sigma(x) = \frac{1}{1 + e^{-x}}\) | (0, 1) | Used for binary classification or probabilistic outputs. | Simple and interpretable (outputs probabilities). | **Vanishing gradient** problem for large/small inputs; slow convergence. |
| **Tanh (Hyperbolic Tangent)** | \(\tanh(x) = \frac{2}{1 + e^{-2x}} - 1\) | (-1, 1) | Commonly used in hidden layers. | Outputs centered around zero, aiding convergence. | **Vanishing gradient** problem for extreme values. |
| **ReLU (Rectified Linear Unit)** | \(\text{ReLU}(x) = \max(0, x)\) | [0, ∞) | Commonly used in hidden layers, especially in deep networks. | Efficient computation, reduces likelihood of vanishing gradient. | **Dying ReLU** problem: neurons can get stuck at zero during training. |
| **Leaky ReLU** | \(\text{Leaky ReLU}(x) = \max(\alpha x, x)\) where \(\alpha\) is a small constant | (-∞, ∞) | Used to avoid **dying ReLU** problem, often in hidden layers. | Allows a small, non-zero gradient for negative inputs, helping to avoid dead neurons. | Still prone to exploding gradients for large \(\alpha\) values. |
| **Parametric ReLU (PReLU)** | \(\text{PReLU}(x) = \max(\alpha x, x)\) where \(\alpha\) is learned during training | (-∞, ∞) | Used in deep learning networks where Leaky ReLU's \(\alpha\) is learned. | Adaptable \(\alpha\) values allow the model to learn the optimal slope for negative values. | Requires additional computation to learn \(\alpha\), and may overfit in some cases. |
| **ELU (Exponential Linear Unit)** | \(\text{ELU}(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha (e^x - 1) & \text{if } x \leq 0 \end{cases}\) | (-\(\alpha\), ∞) | Used in deep networks to improve learning. | Smooth transition from negative to positive outputs. | Computationally more expensive than ReLU. |
| **SELU (Scaled ELU)** | \(\text{SELU}(x) = \lambda (\text{ELU}(x))\) where \(\lambda\) is a scaling factor. | (-\(\alpha\), ∞) | Used in self-normalizing networks. | Helps networks self-normalize; efficient for deep networks. | Works best with specific weight initialization and batch normalization. |
| **Softmax** | \(\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}\) | (0, 1) for each class | Used in the output layer for **multi-class classification**. | Converts logits into probabilities that sum to 1, suitable for multi-class problems. | Sensitive to extreme values, leading to numerical instability. |
| **Swish** | \(\text{Swish}(x) = x \cdot \sigma(x)\) | (-∞, ∞) | Used in deep learning models as an alternative to ReLU. | Smooth non-linearity, avoids **dying ReLU** problem. | Computationally more expensive than ReLU. |

### Explanation of Advantages and Disadvantages:
- **Vanishing Gradient Problem**: Activation functions like sigmoid and tanh suffer from this issue when their inputs are large or small, making gradients near zero and slowing learning.
- **Dying ReLU Problem**: For ReLU, if inputs are negative, it outputs zero and no gradient is propagated, effectively "killing" the neuron.
- **Computation Cost**: Some functions like ELU and Swish are more computationally expensive than simpler functions like ReLU.
- **Probabilistic Output**: Sigmoid and softmax are often used when the output needs to represent probabilities, with softmax used for multi-class classification.

Each activation function has its own strengths, and the best choice depends on the problem you're solving and the network architecture. 😊