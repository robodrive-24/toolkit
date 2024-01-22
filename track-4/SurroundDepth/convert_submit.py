import pickle
import os
import numpy as np
from tqdm import tqdm

# specify the path of the prediction results
root = './pred'
files = os.listdir(root)
pred_depth_dict = {}
for file in tqdm(files):
    with open(os.path.join(root, file), 'rb') as f:
        data = pickle.load(f)
    corruption = file.split('.')[0]
    pred_depth_dict[corruption] = data

np.savez_compressed('./pred.npz', **pred_depth_dict)