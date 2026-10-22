"""
Mini-ResNet for CIFAR-10.

A small convolutional network with one residual (skip) connection, built
with the Keras functional API and trained on the CIFAR-10 image dataset
(32x32 RGB images, 10 classes).
"""
from keras import Model, utils
from keras.datasets import cifar10
from keras.layers import (
    Activation,
    Add,
    Conv2D,
    Dense,
    GlobalAveragePooling2D,
    Input,
    MaxPooling2D,
)

# --- Data ---------------------------------------------------------------
# Labels are integers 0-9 with shape (n, 1). Pixel values are scaled from
# 0-255 to 0-1, which makes training more stable.
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# --- Model --------------------------------------------------------------
inputs = Input(shape=(32, 32, 3))

# Stem: two convolutions extract low-level features, pooling shrinks
# the feature map from 28x28 to 9x9.
x = Conv2D(32, 3, activation="relu")(inputs)
x = Conv2D(64, 3, activation="relu")(x)
x = MaxPooling2D(3)(x)
residual = x  # keep a copy for the skip connection

# Residual block: "same" padding and 64 filters keep the output shape
# identical to `residual`, so both tensors can be added element-wise.
x = Conv2D(64, 3, padding="same")(x)
x = Activation("relu")(x)
x = Conv2D(64, 3, padding="same")(x)
x = Activation("relu")(x)
x = Add()([x, residual])

# Head: one more convolution, then average each feature map to a single
# value and map the result to probabilities for the 10 classes.
x = Conv2D(64, 3, activation="relu")(x)
x = GlobalAveragePooling2D()(x)
outputs = Dense(10, activation="softmax")(x)

model = Model(inputs, outputs, name="mini_resnet")

# Save a diagram of the architecture (requires `pydot` and Graphviz).
utils.plot_model(model, "mini_resnet.png", show_shapes=True)

# --- Training -----------------------------------------------------------
# "sparse_" loss because the labels are integers, not one-hot vectors.
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Plot training and validation accuracy
import matplotlib.pyplot as plt
plt.plot(history.history["accuracy"], label="train accuracy")
plt.plot(history.history["val_accuracy"], label="val accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()