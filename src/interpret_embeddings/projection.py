import sklearn.datasets
import pandas as pd
import numpy as np
import umap
import umap.plot
import matplotlib.pyplot as plt



data, labels, id_to_name = np.load('data/processed_data/genome_embeddings.npz').values()

genome_lookup_table = pd.read_csv('data/raw_proteomes/ncbi_dataset/data/data_summary.tsv', sep='\t')
id_to_taxid = dict(zip(genome_lookup_table['Assembly Accession'], genome_lookup_table['Taxonomy id']))



mapper = umap.UMAP().fit(data)
umap.plot.points(mapper, labels=id_to_name)

plt.show()