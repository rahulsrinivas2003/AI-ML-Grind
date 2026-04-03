# names = []
# NOTE : rm  names.txt and then typing "y" removes the file named names.txt 

# for _ in range(3):

#     names.append(input("Name: "))   

# for name in sorted(names):

#     print(f"Hello, {name}")


#2nd method, to write  #### default value for mode is "r" that is read mode ------------------------------------------------------------------------------------------------------

# name = input("Name: ")

# file = open("names.txt", "a") # "a" stands for append mode, which allows us to add new content to the file without overwriting existing content
# file.write(f"{name}\n") # Write the name to the file, followed by a newline character
# file.close() # Close the file to ensure that the changes are saved and resources are released


#3rd method,  to append ------------------------------------------------------------------------------------------------------

name = input("Name: ")

with open("names.txt", "a") as file:

    file.write(f"{name}\n")

#4th method, to read the file --------------------------------------------------------------------------------


names = []

with open("names.txt") as file:

    for line in file:

        names.append(line.rstrip()) # rstrip() is used to remove any trailing whitespace characters, including the newline character, from the end of the line

for name in sorted(names, reverse=True): # sorted() is used to sort the names in reverse order (Z to A)
    print(f"Hello, {name}")