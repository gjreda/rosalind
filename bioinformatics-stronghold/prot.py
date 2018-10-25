"""
Translating RNA into Protein
http://rosalind.info/problems/prot/
"""

import re


def _make_rna_codon_dict():
    """Rosalind gives us the RNA codon table in text form.
    Convert it to something more Python friendly - a dictionary.
    """
    rna_codon_table = {}
    table = """
    UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G
    """
    for line in re.split(r'\s{2}', table):
        line = line.strip()
        if line != '':
            codon, amino_acid = line.split()
            rna_codon_table[codon] = amino_acid
    return rna_codon_table


def encoded_protein(rna):
    rna_codon_table = _make_rna_codon_dict()

    amino_acids = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino_acids.append(rna_codon_table[codon])
    
    protein = ''.join(amino_acids)
    return protein.split('Stop')[0]


# test it
rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
assert(encoded_protein(rna) == 'MAMAPRTEINSTRING')


with open('data/rosalind_prot.txt', 'r') as f:
    print(encoded_protein(f.read().strip()))