students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"}
]

# gryffindor = [

#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for student in sorted(gryffindor):

#     print(student)

#------------------------ Using Filter function which is similar to map function -------------------------------------------------------------

def is_gryffindor(s):

    return s["house"] == "Gryffindor"

gryffindor = filter(is_gryffindor , students)

for student in sorted(gryffindor , key= lambda s: s["name"]):

    print(student["name"])