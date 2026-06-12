import matplotlib.pyplot as plt
import numpy as np

#Mean, median & Standard deviation
marks= np.array([45, 67, 89, 32, 76, 50,])
print(np.mean(marks))
print(np.median(marks))
print(np.std(marks))

#Pie Chart
subjects = ["Maths", "English", "Science", "Kiswahili", "ICT" ]
students = [12, 8, 10, 6, 4]
dist = [30, 20, 25, 15, 10]

plt.pie(dist,labels=subjects,autopct="%1.1f%%")
plt.title("Favorite subjects")
plt.show()

#Bar graph
Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
sales= [1200, 1500, 1800, 1400, 2000]

plt.bar(Days, sales)
plt.title("Weekly sales perfomance")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

