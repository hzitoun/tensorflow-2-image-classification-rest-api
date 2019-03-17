import tensorflow as tf
from tensorflow import keras
import numpy as np

def train_model(train_images, train_labels):
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=10)

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('\nTest accuracy:', test_acc)
    
    return model


def export_model(model):
    keras.experimental.export_saved_model(model, 'fashion_mnist_classifier')
    

if __name__ == '__main__':
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    
    model = train_model(train_images, train_labels)
    export_model(model)