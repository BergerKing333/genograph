import numpy as np
import pandas as pd
import sourmash
from Bio import SeqIO
import os

fileDir = "genomes/ncbi_dataset/data"
output_file = "similarity_table.csv"
genome_files = [f for f in os.listdir(fileDir) if f.endswith('.fna') or f.endswith('.fa')]

print(os.listdir)
print("Genome files found:")
print(genome_files)
minhash_list = []
genome_names = []
for genome_file in genome_files:
    genome_path = os.path.join(fileDir, genome_file)
    seqs = SeqIO.parse(genome_path, "fasta")
    mh = sourmash.MinHash(n=1000, ksize=31)
    for seq_record in seqs:
        mh.add_sequence(str(seq_record.seq).upper(), force=True)
    minhash_list.append(mh)
    genome_names.append(genome_file)

similarity_matrix = np.zeros((len(genome_names), len(genome_names)))
for i in range(len(minhash_list)):
    for j in range(len(minhash_list)):
        if i == j:
            similarity = 1.0
        elif i > j:
            similarity = similarity_matrix[j][i]
        else:
            similarity = minhash_list[i].jaccard(minhash_list[j])
        similarity_matrix[i][j] = similarity

similarity_df = pd.DataFrame(similarity_matrix, index=genome_names, columns=genome_names)
similarity_df.to_csv(output_file)