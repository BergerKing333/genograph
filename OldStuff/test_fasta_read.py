from Bio import SeqIO

path  = "genomes\\ncbi_dataset\\data\\GCF_000001405.40\\GCF_000001405.40_GRCh38.p14_genomic.fna"
SeqIO.parse(path, "fasta")
records = list(SeqIO.parse(path, "fasta"))
print(records[0].id)