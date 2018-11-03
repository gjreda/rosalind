"""
Open Reading Frames
http://rosalind.info/problems/orf/
"""

from Bio import SeqIO
from typing import List
from prot import _make_rna_codon_dict, encoded_protein
from revc import reverse_complement


def _convert_to_rna(dna: str) -> str:
    return dna.strip().replace('T', 'U')


def _create_protein(strand: str, startpos: int) -> str:
    codon_table = _make_rna_codon_dict()

    protein = ''
    for i in range(startpos, len(strand), 3):
        codon = strand[i:i+3]
        if len(codon) < 3:
            break
        print(i, i+3, codon)
        amino = codon_table[codon]

        if amino == 'Stop':
            return protein
        protein += amino


def find_candidate_proteins(dna: str) -> List[str]:
    rna = _convert_to_rna(dna)
    revcomp = _convert_to_rna(reverse_complement(dna))

    candidate_proteins = set()
    for i in range(len(rna) - 2):
        codon = rna[i:i+3]
        rev_codon = revcomp[i:i+3]

        if codon == 'AUG':
            candidate_proteins.add(_create_protein(rna, startpos=i))
        elif rev_codon == 'AUG':
            candidate_proteins.add(_create_protein(revcomp, startpos=i))
        elif codon == 'AUG' and rev_codon == 'AUG':
            candidate_proteins.add(_create_protein(rna, startpos=i))
            candidate_proteins.add(_create_protein(revcomp, startpos=i))
    return sorted([p for p in candidate_proteins if p is not None])


dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
expected = sorted(['MLLGSFRLIPKETLIQVAGSSPCNLS', 'M', 'MGMTPRLGLESLLE', 'MTPRLGLESLLE'])
assert(find_candidate_proteins(dna) == expected)


with open('data/rosalind_orf.txt') as f:
    for record in SeqIO.parse(f, 'fasta'):
        dna = str(record.seq)
        proteins = find_candidate_proteins(dna)
    print('\n'.join(proteins))