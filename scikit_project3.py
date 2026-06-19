import numpy as np  
from sklearn.cluster import KMeans

#Create training data (no labels)
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
#Step 2: Create model
customer_model = KMeans(n_clusters=2, n_init=10)

#Step 3: Train the model
customer_model.fit(customer_data)

#Step 4: View the results
print(customer_model.labels_)

#step 5: Predict new data
print(customer_model.predict([[28,300]]))
print(customer_model.predict([[30,3000]]))
print(customer_model.predict([[48,5000]]))

#Step 1: Create new model
student_data = np.array([
    [1,30],
    [2,40],
    [3,50],
    [4,60],
    [5,70],
    [6,80],
    [7,90],
    [8,95]
])

#Step 2: Create the model
Student_model = KMeans(n_clusters=3, n_init=10)

#Step 3: Train the model
Student_model.fit(student_data)

#Step 4: View the results
print(Student_model.labels_)

#Step 5: predict new data
print(Student_model.predict([[4,50]]))