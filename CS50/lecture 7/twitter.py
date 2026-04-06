import re 

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url):
    print(f"Username: {matches.group(1)}")

#(?:) non capturing group  , () capturing group 

