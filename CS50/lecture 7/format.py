import re 

name = input("Name: ").strip()

if matches := re.search(r"^(.+), *(.+)$" , name): # the value inside parantheses is called a group and is returned to matches 

    name = matches.group(2) + " " + matches.group(1)

    
print(f"Hello, {name}")

# ":=" is called a walrus operator which allows assigning 
# values from right to left in a conditional statement