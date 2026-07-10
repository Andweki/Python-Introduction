#Multi label classification using pytorch
import tensorflow as tf
import numpy as np

#movie features
#[Action, Comedy, Romance, Adventure]
x = np.array([
    #Action movies
    [95, 90, 80, 75],
    [90, 75, 65, 80],
    [90, 85, 65, 70],

    #Comedy movies
    [80, 90, 75, 65],
    [55, 90, 85, 80],
    [65, 90, 75, 85],
  
    
    #Romance movies
    [70, 80, 90, 85],
    [75, 85, 90, 80],
    [80, 75, 85, 75],
   
   
    #Adventure movies
    [85, 70, 80, 85],
    [80, 85, 75, 90],
    [75, 80, 85, 95],
    ])

y = np.array([
    [1,0,0,1],
    [1,0,0,1],
    [1,0,0,1],

    [0,1,1,0],
    [0,1,1,0],
    [0,1,1,0],

    [1,1,0,1],
    [1,1,0,1],
    [1,1,0,1],

    [1,1,0,1],
    [1,1,0,1],
    [1,1,0,1],
])

#Build the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),  
    tf.keras.layers.Dense(4, activation='sigmoid')
])

#Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

#Train the model
model.fit(x, y, epochs=50, batch_size=4)

#Make predictions
new_movie = np.array([
    [96, 100, 5, 79]
    ])

prediction = model.predict(new_movie)
print("\nprediction probabilities for the new movie: ")
print(prediction)

#Genre names
genres = [
    'Action',
    'Comedy',
    'Romance',
    'Adventure' 
]

print("\nPredicted genres for the new movie: ")
for i in range(len(genres)):
    if prediction[0][i] > 0.5:
        print(genres[i])