import numpy as np

marks= np.array([70, 80, 90, 60, 50,])
print("Marks:", marks)

number=np.array([1, 2, 3, 4, 5])
print(number+10)
print(number*2)

#useful numpy functions
scores=np.array([70, 80, 90, 60, 50])
print(scores)

#Average score
print(np.mean(scores))

#Highest score
print(np.max(scores))

#Lowest score
print(np.min(scores))   

#total score
print(np.sum(scores))

#Middle score
print(np.median(scores))

#variance
print(np.var(scores))

#standard deviation how much the scores deviate from the mean
print(np.std(scores))

#2D array
students=np.array(
    [[70,80,90],
     [60,50,40],
     [85,75,65]]
)
print(students)
print(students[0]) #first row
print(students[1][2]) #second row third column
print(students[:,0]) #first column   