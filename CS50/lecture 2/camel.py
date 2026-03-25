camelcase = input("Enter ur camelcase statement: ")
snakecase = ""

for letter in camelcase:

    if letter.isupper():

        snakecase += "_" + letter.lower()
    else:

        snakecase += letter
print("The Snake case for ur Camelcase variable is:",snakecase )
