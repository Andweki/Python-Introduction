#Regression model using Tensorflow - output is a single value/number
import tensorflow as tf

import numpy as np

#Training data input
study_hours = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
],dtype=float)

#correct answers output
exam_scores = np.array([40,50,60,70,80,90])

#Create the neural network
student_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)), #This tells tensorflow what the data looks like
    tf.keras.layers.Dense(1)
])

#Complete the model, prepare model for training
#sgt Stochastic Gradient Descent

student_model.compile(
    optimizer = "sgd",
    loss = "mean_squared_error"
)

#Training the model
student_model.fit(study_hours,exam_scores,epochs=20)

#Make a prediction
prediction = student_model.predict(np.array([[7.0]]))

print(prediction)