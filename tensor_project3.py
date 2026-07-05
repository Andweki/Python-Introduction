#Multi class classification model using Tensorflow - output is a single value/number
import tensorflow as tf
import numpy as np

#Input data - 4 features(Employee features)
#communication, technical skills, numerical, creativity
x = np.array([
    [90,30,40,50], #HR
    [45,40,95,80], #Finance 
    [35,95,50,40], #IT
    [75,45,40,90], #Marketing
    [88,35,45,60], #HR
    [40,45,90,30], #Finance
    [30,98,55,45], #IT
    [80,40,35,95]  #Marketing
])

#Output data - 4 classes (one hot encoded)
y = np.array([
    0, #HR
    1, #Finance
    2, #IT
    3, #Marketing
    0, #HR
    1, #Finance
    2, #IT
    3   #Marketing
])

#Build our neural network model
model = tf.keras.Sequential([
    #Input layer with 4 features and 16 neurons
    tf.keras.layers.Dense(16, activation='relu'), #Input layer with 4 features and 16 neurons
    tf.keras.layers.Dense(8, activation='relu'),  #Hidden layer with 8 neurons
    #Output layer with 4 classes (one for each department)
    tf.keras.layers.Dense(4, activation='softmax') #Output layer with 4 classes
])

#Compile the model
#Predict numbers regression, use mean_squared_error loss function
#Predict 3 or more classes, use sparse_categorical_crossentropy loss function
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Train the model
model.fit(x, y, epochs=20)

#Make predictions
new_employee = np.array([
    [40, 92, 55, 42]
    ]) #New employee features
prediction = model.predict(new_employee)
print(prediction)