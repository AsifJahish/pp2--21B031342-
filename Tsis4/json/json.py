import json
  
# Opening JSON file
f = open('sample-data.json')

data = json.load(f)

for i in data['totalCount']:
    print(i)
  
# Closing file
f.close()