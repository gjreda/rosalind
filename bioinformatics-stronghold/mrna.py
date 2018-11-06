"""
Inferring mRNA from Protein
http://rosalind.info/problems/mrna/
"""

from prot import _make_rna_codon_dict
from collections import defaultdict

REVERSE_CODON_DICT = {
    'F': ['UUU', 'UUC'],
    'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'M': ['AUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'],
    'H': ['CAU', 'CAC'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'Stop': ['UAA', 'UAG', 'UGA'],
    'Q': ['CAA', 'CAG'],
    'K': ['AAA', 'AAG'],
    'E': ['GAA', 'GAG'],
    'C': ['UGU', 'UGC'],
    'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'W': ['UGG']
}


def _make_reverse_codon_dict():
    # not going to actually call this every time, bc it'd be expensive
    # instead, do it once and persist the data structure, as above
    # execute lookups against the persisted structure
    # this function is just here to show how it's done
    reverse_codon_table = defaultdict(list)
    codon_table = _make_rna_codon_dict()
    for k, v in codon_table.items():
        reverse_codon_table[v].append(k)
    return reverse_codon_table


def num_rna_possibilities(protein: str) -> int:
    n = 3  # Stop codons
    for aa in protein:
        n *= len(REVERSE_CODON_DICT[aa])
    return n % 1000000


assert(num_rna_possibilities('MA') == 12)


with open('data/rosalind_mrna.txt') as f:
    protein = f.read().strip()
    print(num_rna_possibilities(protein))