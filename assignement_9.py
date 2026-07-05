#Bank Loan qualification model using Tensorflow
import tensorflow as tf
import numpy as np


#Input data - 4 features(Employee features)
#Monthly income, credit score, employment duration, existing debt
x = np.array([
    [5000, 700, 2, 10000],
    [6000, 750, 3, 15000],
    [7000, 800, 4, 20000],
    [8000, 850, 5, 25000],
    [9000, 900, 6, 30000],
    [10000, 950, 7, 35000],
    [11000, 1000, 8, 40000],
    [12000, 1050, 9, 45000],
    [13000, 1100, 10, 50000],
    [14000, 1150, 11, 55000]
])

#Output data - 1 value (Loan qualification: 0 = Rejected, 1 = Approved)
y = np.array([[0],
              [0], 
              [0], 
              [0], 
              [1], 
              [1], 
              [1], 
              [1], 
              [1], 
              [1]
              ])

#Build the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'), #Input layer with 10 neurons
    tf.keras.layers.Dense(8, activation='relu' ),  #Hidden layer with 8 neurons

    #Output layer with 1 class (Approved or Rejected)
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

#Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Train the model
model.fit(x, y, epochs=20)

#Make predictions
customer = np.array([
    [120000, 780, 8, 15000]
    ]) 
#New customer features
prediction = model.predict(customer)
if prediction == 0:   
    print("Rejected")
else:
    print("Approved")