import json
import requests
import sys

if (len(sys.argv)) != 2:

    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2)) # json.dumps is used to convert a Python object into a JSON string. The indent parameter is used to specify the number of spaces to use for indentation in the resulting JSON string, making it more readable.


o = response.json()

for result in o["results"]:

    print(result["trackName"])