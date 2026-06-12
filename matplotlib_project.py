import matplotlib.pyplot as plt

#a line graph(x and Y data)
x = [1, 2, 3, 4, 5]
y = [10, 25, 30, 45, 60]

plt.plot(x, y)
plt.title("Growth over time") #title of the graph
plt.show() #display the graph

#bar graph (students and their marks)
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
marks = [85, 90, 92, 78, 88]

plt.bar(students, marks) #create a bar graph
plt.title("Student performance")
plt.show()

#Pie chart (sales distribution)
products = ['Phones', 'Laptops', 'tvs', 'Tablets']#name shown on each slice
sales = [40, 25, 20, 15]  #size of each slice(percentage values)

plt.pie(sales,labels=products, autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()

#scatter plot (study hours vs marks)
study_hours=[1,2,3,4,5] #x-axis (independent variable)
scores=[40,50,65,80,95] #

plt.scatter(study_hours, scores)
plt.title("study hours vs marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

