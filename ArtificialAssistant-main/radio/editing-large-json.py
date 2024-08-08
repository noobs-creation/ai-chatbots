import json
import time

# Opening JSON file
f = open('radio-browser.json', "rb")
 
# returns JSON object as dictionary
data = json.load(f)


di = []
c = 0
for i in data['radio-browser']:
    temp = {}
    if i['country'] == 'India':
        c+=1
        print(i)
        # time.sleep(1)
        temp['country'] = i['country']
        temp['changeuuid'] = i['changeuuid']
        temp['stationuuid'] = i['stationuuid']
        temp['url'] = i['url']
        temp['url_resolved'] = i['url_resolved']
        temp['name'] = i['name']
        temp['countrycode'] = i['countrycode']
        temp['language'] = i['language']
        temp['tags'] = i['tags']
        di.append(temp)

print(di)

# ff = open('radio-browser.json', "rb")
# d = json.load(ff)
d={}
d['final-list'] = di
json.dump(d, open('final-radio-browser.json', 'w'), indent=4)