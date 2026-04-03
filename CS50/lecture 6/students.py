# with open("students.csv") as file:

#     for line in file:

#         name , house = line.rstrip().split(",")

#         print(f"{name} is in {house}") 
#---------------------------------------------------------------------------------------------------------------------------

#using dictionaries 

# students = []

# with open("students.csv") as file:

#     for line in file:

#         name , house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"name" : name , "house":house} # this is a more concise way to create a dictionary with the name and house as key-value pairs}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# # for student in sorted(students, key = get_name): # sorted() is used to sort the students based on their names using the get_name function as the sorting key:

# #     print(f"{student['name']} is in {student['house']}")




# for student in sorted(students, key = lambda student: student["house"]): #lambda is an anonymous function ( meaning a  function that doesnt exist ) that takes student as a parameter and returns the value of the "house" key for that student.
#     # the lambda code is doing the same thing as the one commented right above this loop 
#     print(f"{student['name']} is in {student['house']}")

# Using csv module to read the csv file ------------------------------------------------------------------------------------------------------

import csv 

students = []

# with open("students.csv") as file:

#     reader = csv.reader(file) # csv.reader() is used to create a reader object that can iterate over the lines in the file, parsing them as CSV data.

#     for name, home in reader:

#         students.append({"name": name, "home": home})

with open("students.csv") as file:

    reader = csv.DictReader(file) # csv.DictReader() is used to create a reader object that can iterate over the lines in the file, parsing them as CSV data and returning each row as a dictionary where the keys are the column headers.
    for row in reader:

        students.append(row) # we can access the values in each row using the column headers as keys in the dictionary
for student in sorted(students, key = lambda student: student["name"]):

    print(f"{student['name']} is from {student['home']}")
 


 # To Write to a CSV file ------------------------------------------------------------------------------------------------------

# name = input("Name: ")
# home = input("Home: ")

# with open("students.csv", "a") as file:

#     writer = csv.writer(file)
#     writer.writerow([name,home]) # writerow() is used to write a single row of data to the CSV file, where the data is provided as a list of values corresponding to the columns in the CSV file.

#     writer = csv.DictWriter(file , fieldnames= ["name", "home"]) # fieldnames is used to specify the column headers for the CSV file when using DictWriter. It takes a list of strings that represent the names of the columns in the CSV file.
#     writer.writerow({"name": name, "home": home}) # writerow() is used to write a single row of data to the CSV file, where the data is provided as a dictionary with keys corresponding to the column headers specified in fieldnames.