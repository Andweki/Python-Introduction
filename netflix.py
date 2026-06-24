#Hybrid learning.
import numpy as np

#Categories of content available on netflix
content_types = ["Action", "Romance", "Comedy", "Investigation", "Reality"]

#Number of times user watched each content type
watch_history = np.array([10,3,4,7,1])

#Step 1
#Get the index of the highest watched category
top_index = np.argmax(watch_history)

#Convert index to content name
preferred_content = content_types[top_index]

#Step 2 Calculate preference scores
#Total watch activity across all categories
total_watches = sum(watch_history)

#Dict to store preference strength for each category
scores = {}
for i in range(len(content_types)):
    #preference formula-score=watch_history[i]/total_watches
    scores[content_types[i]]=watch_history[i]/total_watches

#step 3 - Display user behavior
print("\nUSER WATCH ANALYSIS")

for i in range(len(content_types)):
    print(content_types[i], "watched:", watch_history[i])

print("\nTOTAL WATCH TIME:", total_watches)
print("\nTOP PREFERENCE:")
print(preferred_content)
print("\nRECOMMENDATIONS:")
for i in range(len(content_types)):
    if content_types[i] == preferred_content:
        print(content_types[i], "->HIGH PRIORITY(recommend more of this type)")
    else:
        print(content_types[i], "->LOW PRIORITY")
