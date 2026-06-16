#supervised learning
#Learning using labeled data
#The model learns the relationship between x and y
x=[[30], [40], [50], [60], [70], [80], [90]] #input data (marks)
y=["FAIL", "FAIL", "PASS", "PASS", "PASS", "PASS", "PASS"] #Output labels

a=[[16],[17],[18],[19],[20],[25]]
b=["No","No","Yes","Yes","Yes","Yes"]

#In summary supervised learns from answers

#Unsupervised learning
#Learning from data without labels
#The AI finds patterns or groups 

import numpy as np
#Age spending behavior

data=np.array([
    [20,200]
    [22,250]
    [25,300]
    [40,2000]
    [45,2500]
    [50,3000]
])

#Study hours vs marks
data2=np.array([
    [1,30]
    [2,40]
    [3,50]
    [5,80]
    [6,90]
    [7,95]
])

#Reinforcment learning
#Learning through rewards and feedback
#No dataset labels, just actions and rewards

actions=["jump","run","duck"]
rewards=(
    "jump":10,
    "run":5,
    "duck":8
)