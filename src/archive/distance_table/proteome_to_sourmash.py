import sourmash
import glob
import os
import pandas as pd
import numpy as np
from Bio import SeqIO
import screed

KSIZE = 10
SCALED = 200
PROTEIN = True


all_protein_files = [f.replace('\\', '/') for f in glob.glob('genomes/ncbi_dataset/data/GCF*/protein.faa')]

for i, pf in enumerate(all_protein_files):
    mh = sourmash.MinHash(n=0, ksize=KSIZE, scaled=SCALED, is_protein=PROTEIN)

    try:
        with screed.open(pf) as seqFile:
            for record in seqFile:
                mh.add_protein(record.sequence)
    except Exception as e:
        print(f'** ERROR with file {pf}: {e}')
        continue

    sig_name = os.path.dirname(pf).split('/')[-1]
    sig = sourmash.SourmashSignature(mh, name=sig_name)

    out_fp = f'proteome_sigs/{sig_name}.sig'

    with open(out_fp, 'w') as fp:
        sourmash.save_signatures([sig], fp)

    if i % 10 == 0:
        print(f'... processed {i} / {len(all_protein_files)}')
