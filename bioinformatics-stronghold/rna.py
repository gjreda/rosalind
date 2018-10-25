"""
Problem ID: RNA
http://rosalind.info/problems/rna/

Transcribing DNA into RNA
"""

def transcribe_dna_to_rna(s):
    return s.strip().replace('T', 'U')


s = 'GATGGAACTTGACTACGTAAATT'
assert(transcribe_dna_to_rna(s) == 'GAUGGAACUUGACUACGUAAAUU')


with open('data/rosalind_rna.txt', 'r') as f:
    print(transcribe_dna_to_rna(f.read()))