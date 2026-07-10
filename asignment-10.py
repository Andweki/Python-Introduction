#Build a TensorFlow model to predict whether a student will pass an exam.
import tensorflow as tf 
import numpy as np
from sklearn.model_selection import train_test_split

#student featres
#[Study hours, Attendance percentage, Assignment score]

x = np.array([
    [10, 50, 66],
    [11, 58, 69],
    [12, 63, 70],
    [13, 65, 79],
    [14, 73, 72],
    [15, 65, 75],
    [16, 68, 78],
    [17, 70, 80],
    [8, 50, 59],
    [11, 43, 62],
    [14, 73, 75],
    [16, 80, 90]

])

#0 failed, 1 passed
y = np.array([
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,

])

#Split the data set
x_train, x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

#Build the neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='relu'),  
    tf.keras.layers.Dense(1, activation='sigmoid')
])

#Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

#Train the model
model.fit(x_train,y_train,epochs=150)

#Evaluate the model
loss,accuracy=model.evaluate(x_test,y_test)

print("Loss:", loss)
print("Accuracy:", accuracy)

#Prediction
new_student = np.array([
    [15,68,70]
])
#Compare the predicted labels


prediction = model.predict(new_student)
# pred_val = float(prediction)
print("Prediction", prediction)
# print(pred_val)
# if float(prediction) >= 0.5:
#     print("passed")
# else:
#     print("failed")