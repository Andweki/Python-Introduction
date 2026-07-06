import tensorflow as tf
import numpy as np

#Student features - input data
#[Mathematics, English, Science, Aptitude test]

x = np.array([
    #Computer Science students
    [95, 90, 80, 75],
    [90, 75, 65, 80],
    [90, 85, 65, 70],
    [80, 65, 70, 65],
    [92, 80, 85, 60],

    #Business students
    [80, 90, 75, 65],
    [55, 90, 85, 80],
    [65, 90, 75, 85],
    [85, 88, 80, 75],
    [70, 95, 80, 85],
    
    #Engineering students
    [70, 80, 90, 85],
    [75, 85, 90, 80],
    [80, 75, 85, 75],
    [85, 70, 95, 80],
    [60, 65, 80, 75],
   
    #Education students
    [85, 70, 80, 85],
    [80, 85, 75, 90],
    [75, 80, 85, 95],
    [60, 75, 80, 85],
    [75, 60, 65, 80]
])

#Degree program 
# output data - 1 value 
# 0 = Computer Science,
# 1 = Business,
# 2 = Engineering, 
# 3 = Education

y = np.array([
    0,0,0,0,0,
    1,1,1,1,1,
    2,2,2,2,2,
    3,3,3,3,3
])

#Build the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu'), #Input layer with 16 neurons
    tf.keras.layers.Dense(8, activation='relu' ),  #Hidden layer with 8 neurons

    #Output layer with 4 classes (Computer Science, Business, Engineering, Education)
    tf.keras.layers.Dense(4, activation='softmax'),
])

#Compile the model
model.compile(
    optimizer='adam', 
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
    )

#Train the model
model.fit(x, y, epochs=50)

#Make predictions
new_student = np.array([
    [92, 80, 90, 89]  # Example student scores
])
prediction = model.predict(new_student)
print("Prediction probabilities:", prediction)
#print(prediction)

# Get the predicted class (degree program)
predicted_class = np.argmax(prediction)

degrees = ["Computer Science", "Business", "Engineering", "Education"]
print(f"Recommended degree program: {degrees[predicted_class]}")