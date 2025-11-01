import sourmash
import glob
import pandas as pd
import numpy as np

ref_table = pd.read_csv('genomes/ncbi_dataset/data/data_summary.tsv', sep='\t')
id_to_name = dict(zip(ref_table['Assembly Accession'], ref_table['Organism Common Name']))


signature_files = [f.replace('\\', '/') for f in glob.glob('proteome_sigs/*.sig')]

sigs = []
for sf in signature_files:
    sigs.extend(sourmash.load_signatures(sf))

print(f'loaded {len(sigs)} signatures')

dist_matrix = sourmash.compare.compare_all_pairs(sigs, ignore_abundance=True)


df = pd.DataFrame(dist_matrix, index=[sig.name for sig in sigs], columns=[sig.name for sig in sigs])

np.savez('signature_distance_table.npz', data=dist_matrix, sig_names=[sig.name for sig in sigs])

df.index = [id_to_name.get(sig.name, sig.name) for sig in sigs]
df.columns = [id_to_name.get(sig.name, sig.name) for sig in sigs]


# print(df)
df.to_csv('signature_distance_table.csv')