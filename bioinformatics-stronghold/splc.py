"""
RNA Splicing
http://rosalind.info/problems/splc/
"""

from Bio import SeqIO
from prot import _make_rna_codon_dict, encoded_protein
from typing import List


def remove_introns(dna: str, introns: List[str]) -> str:
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna


with open('data/rosalind_splc.txt', 'r') as f:
    introns = []
    for i, record in enumerate(SeqIO.parse(f, 'fasta')):
        if i == 0:
            dna = str(record.seq)
            continue
        introns.append(str(record.seq))
    
rna = remove_introns(dna, introns).replace('T', 'U')
print(encoded_protein(rna))