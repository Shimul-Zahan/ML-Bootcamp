import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf  # type: ignore
from tensorflow.keras import layers # type: ignore
from tensorflow.keras import backend as K  # type: ignore

# Step 1: ইমেজ লোড করা
image = cv2.imread('/content/images.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR থেকে RGB তে রূপান্তর
image = cv2.resize(image, (64, 64))  # ইনপুট শেপের সাথে মিলানোর জন্য রিসাইজ

# Step 2: ইমেজকে টেন্সরে রূপান্তর
input_image = np.expand_dims(image, axis=0)  # ব্যাচ ডাইমেনশন যোগ করা
input_image = tf.image.convert_image_dtype(input_image, tf.float32)

print(input_image.shape)


# Step 3: প্রথম Conv2D লেয়ার
conv1 = layers.Conv2D(32, (5, 5), activation='relu', input_shape=(64, 64, 3))(input_image)
print(f"Conv1 Shape: {conv1.shape}")

# Step 4: প্রথম MaxPooling
pool1 = layers.MaxPooling2D((2, 2))(conv1)
print(f"Pool1 Shape: {pool1.shape}")

# Step 5: দ্বিতীয় Conv2D লেয়ার
conv2 = layers.Conv2D(64, (5, 5), activation='relu')(pool1)
print(f"Conv2 Shape: {conv2.shape}")

# Step 6: দ্বিতীয় MaxPooling
pool2 = layers.MaxPooling2D((2, 2))(conv2)
print(f"Pool2 Shape: {pool2.shape}")

# Step 7: আউটপুট দেখানো
def display_feature_maps(feature_maps, title):
    feature_maps = K.eval(feature_maps)
    num_filters = feature_maps.shape[-1]
    fig, axs = plt.subplots(4, 8, figsize=(15, 8))
    fig.suptitle(title)
    for i in range(32):  # প্রথম ৩২টি ফিল্টার দেখানোর জন্য
        ax = axs[i//8, i%8]
        ax.imshow(feature_maps[0, :, :, i], cmap='viridis')
        ax.axis('off')
    plt.show()

# Step 8: আউটপুট দেখানো
display_feature_maps(conv1, "Conv1 Feature Maps")
display_feature_maps(pool1, "Pool1 Feature Maps")
display_feature_maps(conv2, "Conv2 Feature Maps")
display_feature_maps(pool2, "Pool2 Feature Maps")
