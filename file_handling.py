#Basic File Handling

#Create file and overwrite existing content
file = open("data.txt", "w")
file.write("Hello, This is first line.\n")
file.close()

#append new content without deleting old data
file = open("data.txt", "a")
file.write("Hello, This is second line\n") 
file.close()

#Reads the file content
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()