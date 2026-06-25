#student dataset
#Each row is a student. 
#Each column represents subject marks.
axis0 = 0 #row
axis1 = 1 #column

import numpy as np 

student = np.array([
    [85, 90, 92],
    [78, 88, 90],
    [92, 85, 88],
    [80, 82, 84],
    [88, 90, 91]
])

#average per student
avg_student = np.mean(student, axis=1)
print("Average marks per student:", avg_student)

#average per subject
avg_subject = np.mean(student, axis=0)
print("Average marks per subject:", avg_subject)

#highest mark in class``
max_student = np.max(student)
print("Highest mark in class:", max_student)

#lowest mark in class
min_student = np.min(student)
print("Lowest mark in class:", min_student)

#arg means index of the maximum value
best_student = np.argmax(avg_student)
print("Best student index:", best_student)

#worst student index
worst_student = np.argmin(avg_student)  
print("Worst student index:", worst_student)

#pass/fail based on average marks
passed = avg_student >= 85
print(passed)

#count how many students passed
print(np.sum(passed))


sales=np.array([
    [200, 150, 300],
    [120, 180, 250],
    [300, 400, 500],
    [100, 90, 80],
    [220, 210, 190]
    ])

#total sales per person
total_sales = np.sum(sales, axis=1)
print("Total sales per person:", total_sales)

#total sales per product
total_product = np.sum(sales, axis=0)
print("Total sales per product:", total_product)

best=np.argmax(total_sales)
print(best)

worst=np.argmin(total_sales)
print(worst)