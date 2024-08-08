import json
import time

# Opening JSON file
f = open('radio_place.json', "rb")
 
# returns JSON object as
# a dictionary
data = json.load(f)

for i in data['radio-list']:
    print(i['country'], i['url'])
    time.sleep(20)

