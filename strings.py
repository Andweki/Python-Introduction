language="python"
print(language)

#string indexing allows you to access individual characters in a string using their position
print(language[0]) #first character
print(language[4]) #fifth character

#string length gives the number of characters in a string
password="3dhpuPxc!"
print(len(password)) #length of the string

word="house"
print(len(word)) #length of the string

#upper() method converts a string to uppercase
location="nairobi"
print(location.upper()) #convert to uppercase

#lower() method converts a string to lowercase
school="LetsCode"
print(school.lower()) #convert to lowercase

#title() method converts the first character of each word to uppercase
full_name="john doe"
print(full_name.title()) #convert to title case

#strip() method removes any leading and trailing whitespace from a string
name="   Brian   "
print(name.strip()) #remove leading and trailing whitespace 

#replace() method replaces a specified value with another value in a string
text="I love javascript"
print(text.replace("javascript", "python")) #replace "javascript" with "python"

#string concatenation allows you to combine two or more strings together
#using the + operator to concatenate strings
greetings="Hello"
person="James"
print(greetings +" " +person)

#f-strings allow you to embed expressions inside string literals, using curly braces {}.
student_name="John Doe"
student_age=20
print(f"My name is {student_name} and I am {student_age} years old.")   

amount=1000
balance=4000
print(f" {amount}is successfully processed and your new balance is {balance}.")
