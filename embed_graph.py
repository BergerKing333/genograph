from pecanpy.pecanpy import DenseOTF
import numpy as np
import pandas as pd

P = 1.0
Q = 1.0
DIMENSIONS = 64
WALK_LENGTH = 80
NUM_WALKS = 10
WORKERS = 4

g = DenseOTF(
    p=P,
    q=Q,
    workers=WORKERS
)

g.read_npz('signature_distance_matrix.npz', weighted=True)

walks = g.simulate_walks(
    walk_length=WALK_LENGTH,
    num_walks=NUM_WALKS
)
embeddings = g.embed()

pd.DataFrame(embeddings).to_csv("genome_embeddings.emb", header=False, index=False)
print("Embeddings saved to 'genome_embeddings.emb'")