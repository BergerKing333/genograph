from pecanpy.pecanpy import DenseOTF
import numpy as np
import pandas as pd

P = 1.0
Q = 1.0
DIMENSIONS = 10
WALK_LENGTH = 80
NUM_WALKS = 50
WORKERS = 4

g = DenseOTF(
    p=P,
    q=Q,
    workers=WORKERS
)

g.read_npz('data/processed_data/signature_distance_table.npz', weighted=True)

embeddings = g.embed(
    dim=DIMENSIONS,
    walk_length=WALK_LENGTH,
    num_walks=NUM_WALKS
)
# pd.DataFrame(embeddings).to_csv("data/processed_data/genome_embeddings.emb", header=False, index=False)

labels = np.load('data/processed_data/signature_distance_table.npz')['sig_names']

ref_table = pd.read_csv('data/raw_proteomes/ncbi_dataset/data/data_summary.tsv', sep='\t')
id_to_name = dict(zip(ref_table['Assembly Accession'], ref_table['Organism Common Name']))


np.savez('data/processed_data/genome_embeddings.npz', embeddings=embeddings, labels=labels, id_to_name=[id_to_name.get(label, label) for label in labels])


print("Embeddings saved to 'data/processed_data/genome_embeddings.npz'")