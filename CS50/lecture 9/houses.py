students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cedric", "house": "Hufflepuff"},
    {"name": "Luna", "house": "Ravenclaw"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in houses:

    print(house)
