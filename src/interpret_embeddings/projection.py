import sklearn.datasets
import pandas as pd
import numpy as np
import umap
import umap.plot
import matplotlib.pyplot as plt

data = pd.read_csv("data/processed_data/genome_embeddings.emb", header=None).to_numpy()[0:5]

mapper = umap.UMAP().fit(data)

labels = pd.read_csv("data/processed_data/signature_distance_table.csv").columns[1:6].to_numpy()


umap.plot.points(mapper, labels=labels)

plt.show()