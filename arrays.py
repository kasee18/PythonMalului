#arrays are specific to datatypes/no mixture ups
courses = ["FullStack", "Cybersecurity", "Datascience"]
print(courses) #printing all courses
print(courses[1]) #printing cybersecurity only

courses.append("UI/UX") #introducing a new course
print(courses)

courses.remove("Datascience") #deleting a specific course
print(courses)

for x in courses: #printing elements one at a time
    print(x)
