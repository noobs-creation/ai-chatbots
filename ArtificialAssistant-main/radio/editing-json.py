import json
import time

# Opening JSON file
f = open('radio_place.json', "rb")
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
'''
# Iterating through the json
# list
# for i in data['radio-list']:
#     print(i)

# for i in data['radio-list']:
#     print('\nsdfsdfsdfs')
#     print(i['country'])
#     time.sleep(5)

# for i in data['radio-list']:
#     print(i['geo'])
'''
c=-1

for i in data['radio-list']:
    c+=1
    print(str(c) + '\t')

# time.sleep(3)

c=-1
for i in data['radio-list']:
    c+=1
    print(str(c) + '\t')
    if i['country'] == 'India':
        pass
    elif i['country'] == 'United Kingdom':
        pass
    elif i['country'] == 'Russia':
        pass
    elif i['country'] == 'United States':
        pass
    elif i['country'] == 'Australia':
        pass
    elif i['country'] == 'Bangladesh':
        pass
    elif i['country'] == 'Canada':
        pass
    else:
        print(i['country'] + str(c))
        data['radio-list'].pop(c)

# for i in data['radio-list']:
#     print(i['country'])

json.dump(data, open('radio_place.json', 'w'), indent=4)

# Closing file
f.close()