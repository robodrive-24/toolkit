import json
import os

# please specify your path here
folder = 'pred'
files = os.listdir(folder)

all_dict = {}
for file in files:
    path = os.path.join(folder, file)
    with open(path, 'r') as f:
        data = json.load(f)
    all_dict[file.split('_results')[0]] = data
    
with open('pred.json', 'w') as f:
    json.dump(all_dict, f)