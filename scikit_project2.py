from sklearn.tree import DecisionTreeClassifier

#Creatiing training data
customer_data = [
    [20,1500],
    [22,18000],
    [25,25000],
    [30,40000], 
    [35,50000], 
    [40,60000], 
    [45,70000],
    [50,80000]
]
loan_results = [
    "Rejected",
    "Rejected",
    "Rejected",
    "Approved",
    "Approved",
    "Approved",
    "Approved",
    "Approved"
]

#Creating the AI model
loan_predictor = DecisionTreeClassifier()

#Train the Model
loan_predictor.fit(customer_data, loan_results)

#Make predictions
print(loan_predictor.predict([[28,35000]]))
print(loan_predictor.predict([[19,12000]]))
print(loan_predictor.predict([[45,75000]]))


#Project 2 Employee hiring predictor
#Create training data
candidate_data = [
    [1,40],
    [2,50],
    [3,55],
    [4,65],
    [5,75],
    [6,85],
    [7,90],
    [8,95]
]

hiring_results = [
    "Rejected",
    "Rejected",
    "Rejected",
    "Hired",
    "Hired",
    "Hired",
    "Hired",
    "Hired"
]
#Creating AI Model

hiring_predictor = DecisionTreeClassifier()

#Train the Model
hiring_predictor.fit(candidate_data,hiring_results)

#Make predictions
print(hiring_predictor.predict([[2,45]]))
print(hiring_predictor.predict([[5,80]]))
print(hiring_predictor.predict([[7,90]]))
