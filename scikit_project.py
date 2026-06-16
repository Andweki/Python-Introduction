from sklearn.tree import DecisionTreeClassifier
#Training data

x=[[30], [40], [50], [60], [70], [80], [90]] #input data (marks)

y=["FAIL", "FAIL", "PASS", "PASS", "PASS", "PASS", "PASS"] #Output

#Create model
model=DecisionTreeClassifier()

#Training the model
model.fit(x,y)
#The model studies the relationship between marks and results
#It learns the patterns automatically and makes predictions

prediction=model.predict(([[75]]))
print(prediction)
print(model.predict([[35]]))
print(model.predict([[55]]))
print(model.predict([[20]]))
print(model.predict([[100]]))

#Training data ->Create model -> Train model -> Make predictions

movie_ratings=[[1],[2],[3],[4],[5]]
customer_opinions=["Dislike","Dislike","Like","Like","Like"]

movie_predictor=DecisionTreeClassifier()
movie_predictor.fit(movie_ratings,customer_opinions)

print(movie_predictor.predict([[0]]))
print(movie_predictor.predict([[6]]))
