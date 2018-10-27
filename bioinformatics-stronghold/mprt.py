"""
Finding a Protein Motif
http://rosalind.info/problems/mprt
"""

import requests
from Bio import SeqIO
from io import StringIO
from argparse import ArgumentParser
import re

FASTA_URL = 'http://www.uniprot.org/uniprot/{}.fasta'
N_glycosylation_regex = r'(?=(N[^P][ST]+[^P]))'


def fetch_motifs(protein_id, motif_regex):
    response = requests.get(FASTA_URL.format(protein_id))
    response.raise_for_status()

    record = list(SeqIO.parse(StringIO(response.text), 'fasta'))[0]
    sequence = str(record.seq)
    matches = re.finditer(motif_regex, sequence)
    if matches:
        return [m.start() + 1 for m in matches]
    return 


if __name__ == '__main__':
    fout = open('data/answer.txt', 'w')
    with open('data/rosalind_mprt.txt', 'r') as fin:
        for line in fin:
            protein = line.strip()
            motifs = fetch_motifs(protein, N_glycosylation_regex)

            if not motifs:
                continue
            
            fout.write(protein + '\n')
            fout.write(' '.join([str(m) for m in motifs]) + '\n')
    fout.close()