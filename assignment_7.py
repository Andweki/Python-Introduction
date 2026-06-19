from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.cluster import KMeans

#Scholarship approval predictor
#Data

marks_percent = ([
    [20,25],
    [25,34],
    [30,45],
    [40,53],
    [50,60],
    [60,71],
    [70,79],
    [80,85]
])


#Train the model

results = ([
    "Rejected",
    "Rejected",
    "Rejected",
    "Rejected",
    "Rejected",
    "Approved",
    "Approved",
    "Approved"
])

#Create AI Model
scholar_app = DecisionTreeClassifier()

#Train the model

scholar_app.fit(marks_percent, results)

#Make predictions
print(scholar_app.predict([[44,60]]))
print(scholar_app.predict([[74,69]]))
print(scholar_app.predict([[90,50]]))

#New Dataset (Gym membership)
#Create training data

gym_data = np.array([
    [18,23],
    [20,26],
    [22,27],
    [25,30],
    [40,20],
    [45,20],
    [50,15],
    [55,10]
])

#Step 2: Create model
gym_model = KMeans(n_clusters=2, n_init=10)

#Train the model
gym_model.fit(gym_data)

# #predict new data
print(gym_model.predict([[23,28]]))
print(gym_model.predict([[34,21]]))
print(gym_model.predict([[64,17]]))