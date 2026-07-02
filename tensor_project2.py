#Classification model using Tensorflow - output is a single value/number
#Binary classification model using Tensorflow - output is a single value/number
import tensorflow as tf 
import numpy as np

#Create the trainin data
x = np.array([
    [1,45],
    [2,55],
    [3,60],
    [4,68],
    [5,72],
    [6,80],
    [7,90]
])

#0 means no, 1 means yes
y = np.array([
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [1]
])

#Build the nueral network model
model = tf.keras.Sequential([
    #input layer - 2 input features
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='relu'),

    #Output layer - single value output
    tf.keras.layers.Dense(1, activation='sigmoid')
])

#Compile the model
model.compile(
    optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']
    )

#Train the model
model.fit(x, y, epochs=100)

#Test the model
predictions = model.predict(np.array([[5, 78]]))
print(predictions)