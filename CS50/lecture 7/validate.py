# email = input("Email: ").strip()
# username , domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

import re 

email = input("Email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email.lower() , re.IGNORECASE):
    print("Valid")

else:

    print("Invalid")