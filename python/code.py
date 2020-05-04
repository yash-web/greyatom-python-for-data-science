# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings

new_class=class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print(new_class)


# Create the Dictionary

courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}
print(courses)
Total=0
for i in courses:
    Total=Total+courses[i]
# Slice the dict and stores  the all subjects marks in variable
print(Total)
percentage=Total/5
print(percentage)

student={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
# Store the all the subject in one variable `Total`
max_marks_scored=max(courses,key=courses.get)
print(max_marks_scored)
topper=max(student,key=student.get)
print(topper)
k=topper.split()
# Print the total
first_name=k[0]
last_name=k[1]
print(first_name)
print(last_name)
# Insert percentage formula
full_name=first_name+' '+last_name
x=first_name.upper()
print(x)
y=last_name.upper()
print(y)

certificate_name=y+' '+x
print(certificate_name)
# Print the percentage




# Create the Dictionary
 



# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


