import pandas as pd
import json

ref_table = pd.read_csv('genomes/ncbi_dataset/data/data_summary.tsv', sep='\t')
# print(ref_table)
print(ref_table['Assembly Accession'])

accession_to_name = dict(zip(ref_table['Assembly Accession'], ref_table['Organism Common Name']))

tbl = pd.read_csv("similarity_table.csv", index_col=0)

tbl.columns = [accession_to_name.get(col.split('_')[0] + "_" + col.split('_')[1], col) for col in tbl.columns]
tbl.index = [accession_to_name.get(idx.split('_')[0] + "_" + idx.split('_')[1], idx) for idx in tbl.index]

print(tbl)