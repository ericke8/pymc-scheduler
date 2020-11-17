import json
import random
import datetime

path = 'schema.json'

with open(path) as f:
  data = json.load(f)

officer = data['officers']
inductee = data['inductees']

for o in officer:


officer_rand = random.sample(officers, len(officers))

for o in officer:
  print(o)
  for i in inductee:
    print(i)
    

print(officer)
print(inductee)