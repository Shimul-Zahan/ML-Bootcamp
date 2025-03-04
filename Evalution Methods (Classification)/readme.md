# Classification Evaluation Metrics

In this document, we cover the common evaluation metrics used in classification problems to assess model performance, particularly when working with imbalanced datasets.

## 1. **Accuracy**
**Definition**: The ratio of correctly predicted instances to the total instances in the dataset.
**Formula**:
\[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
\]
**Use Case**: Suitable for balanced datasets.

## 2. **Precision**
**Definition**: The ratio of correctly predicted positive observations to the total predicted positives.
**Formula**:
\[
Precision = \frac{TP}{TP + FP}
\]
**Use Case**: Important when minimizing false positives is crucial (e.g., spam detection).

## 3. **Recall (Sensitivity)**
**Definition**: The ratio of correctly predicted positive observations to the all observations in the actual class.
**Formula**:
\[
Recall = \frac{TP}{TP + FN}
\]
**Use Case**: Important when minimizing false negatives is critical (e.g., fraud detection).

## 4. **F1-Score**
**Definition**: The harmonic mean of Precision and Recall, balancing both metrics.
**Formula**:
\[
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
\]
**Use Case**: Useful when both Precision and Recall are important (e.g., fraud detection).

## 5. **Confusion Matrix**
**Definition**: A table that describes the performance of a classification model by comparing the actual and predicted values.
**Components**:
- **TP**: True Positive
- **TN**: True Negative
- **FP**: False Positive
- **FN**: False Negative

**Use Case**: To get more granular insight into model errors.

## 6. **AUC-ROC (Area Under Curve - Receiver Operating Characteristic)**
**Definition**: A performance measurement for classification problem at various thresholds settings.
**Formula**: The area under the ROC curve.
**Use Case**: Useful for evaluating classifiers in imbalanced datasets.

## 7. **ROC Curve**
**Definition**: A graphical plot that shows the true positive rate (TPR) against the false positive rate (FPR).
**Use Case**: To visualize the trade-off between true positives and false positives.

## 8. **Log Loss**
**Definition**: Measures the uncertainty of the predictions, penalizing incorrect classifications with higher confidence.
**Formula**:
\[
Log Loss = - \frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]
\]
**Use Case**: Used in binary classification with probabilistic outputs.

## Conclusion
When working with classification tasks, especially with imbalanced datasets, metrics such as **F1-Score**, **Precision**, **Recall**, and **AUC-ROC** are often more informative than accuracy alone. These metrics help ensure the model is performing well across both classes (e.g., fraudulent and legitimate transactions).

---

**Real-life example: Fraud Detection**

```python
# Example of how to compute these metrics in a fraud detection scenario
