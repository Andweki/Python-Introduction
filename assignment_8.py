# You tube recommendation system

import numpy as np

#Categories of content available on youtube
content_category = ["Technology", "Education", "Gaming", "Music", "Sports"]

watch_time = np.array([19,7,9,4,11])

#Most watched Category
top_video = np.argmax(watch_time)
# print(top_video)

#convert top video index to category
top_category = content_category[top_video]
# print(top_category)

#Calculate total watch time
total_watch = sum(watch_time)
# print(total_watch)

# Find the preference score for each category
preference_score = {}
for i in range(len(content_category)):
   preference_score[content_category[i]] = watch_time[i] / total_watch

# Display
print("\nCATEGORY WATCH COUNT")

for i in range(len(content_category)):
   print(content_category[i], "Watched", watch_time[i])

print("\nTotal Watched Hours", total_watch,"\n")
print("Top Watched Category", top_category,"\n")
