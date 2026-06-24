import numpy as np  
from sklearn.cluster import KMeans

#Create the data
viewer_data = np.array([
    [15,5],
    [16,6],
    [18,8],
    [20,10],
    [35,25],
    [40,30],
    [45,35],
    [50,40]
])
#Create the model
viewer_model = KMeans(n_clusters=2,n_init=10)

#Train the model
viewer_model.fit(viewer_data)

#Display cluster labels
cluster_names = {
    0:"Older Gen",
    1:"Younger Gen"
}
for cluster in viewer_model.labels_:
    print(cluster_names[cluster])

#Predict the viewer
prediction = viewer_model.predict([[17,7]])
print(cluster_names[prediction[0]])

#Project 2
#Step 1 create the data
customer_data = np.array([
    [18,200],
    [20,250],
    [22,300],
    [25,350],
    [40,2000],
    [45,2500],
    [50,3000],
    [55,3500]
])

#Create the model
spending_model = KMeans(n_clusters=3,n_init=10)

#Train the model
spending_model.fit(customer_data)

#Display cluster labels
cluster_names = {
    0:"Low spenders",
    1:"Medium spenders",
    2:"High spenders"
}

for cluster in spending_model.labels_:
    print(cluster_names[cluster])