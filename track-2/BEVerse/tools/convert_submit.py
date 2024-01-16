import pickle
import os

## specify the folder where the results are saved
folder = './test'
corruptions = os.listdir(folder)

all_preds = {}
for corruption in corruptions:
    with open(os.path.join(folder, corruption, 'results.pkl'), 'rb') as f:
        pred = pickle.load(f)
    all_preds[corruption] = pred
    
with open('pred.pkl', 'wb') as f:
    pickle.dump(all_preds, f)