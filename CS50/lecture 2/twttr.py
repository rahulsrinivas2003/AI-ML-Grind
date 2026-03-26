statement = input("Input: ")
result = ""

for letter in statement:
    if letter.lower() not in "aeiou":
        result += letter

print(result)
