import sklearn.datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data, labels = np.load('data/processed_data/genome_embeddings.npz').values()

vec = {name: v for name, v in zip(labels, data)}

def distance_between_embeddings(name1, name2):
    v1 = vec[name1]
    v2 = vec[name2]
    return np.linalg.norm(v1 - v2)


df = pd.DataFrame(index=labels, columns=labels)
for name1 in labels:
    for name2 in labels:
        df.loc[name1, name2] = distance_between_embeddings(name1, name2)

df.to_csv("data/processed_data/embedding_space_distance_table.csv")