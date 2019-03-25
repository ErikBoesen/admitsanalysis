import json

with open('old.json', 'r') as f:
    old = json.load(f)
with open('new.json', 'r') as f:
    new = json.load(f)
for name in old:
    if name not in new:
        print(name)
