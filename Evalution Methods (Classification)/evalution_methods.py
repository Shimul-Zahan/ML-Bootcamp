import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, roc_auc_score, confusion_matrix, roc_curve, auc

# Sample data for actual and predicted values (fraud detection example)
actual = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0])  # Actual values (0: Legitimate, 1: Fraudulent)
predicted = np.array([0, 1, 0, 0, 0, 1, 1, 0, 1, 1])  # Predicted values

# 1. Accuracy
accuracy = accuracy_score(actual, predicted)
print(f"Accuracy: {accuracy:.2f}")

# 2. Precision
precision = precision_score(actual, predicted)
print(f"Precision: {precision:.2f}")

# 3. Recall
recall = recall_score(actual, predicted)
print(f"Recall: {recall:.2f}")

# 4. F1-Score
f1 = f1_score(actual, predicted)
print(f"F1-Score: {f1:.2f}")

# 5. Confusion Matrix
conf_matrix = confusion_matrix(actual, predicted)
print(f"Confusion Matrix:\n{conf_matrix}")

# 6. AUC-ROC
roc_auc = roc_auc_score(actual, predicted)
print(f"AUC-ROC: {roc_auc:.2f}")

# 7. ROC Curve
fpr, tpr, thresholds = roc_curve(actual, predicted)
roc_auc_curve = auc(fpr, tpr)

print(f"AUC (using ROC curve): {roc_auc_curve:.2f}")

# Optional: Plotting ROC Curve (Optional)
import matplotlib.pyplot as plt

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc_curve:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
