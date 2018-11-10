"""
Transitions and Transversions
http://rosalind.info/problems/tran/
"""

from Bio import SeqIO


def transition_tranversion_ratio(s1: str, s2: str) -> float:
    transition_map = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
    transversion_map = {'A': ['C', 'T'], 
                        'C': ['A', 'G'], 
                        'G': ['C', 'T'],
                        'T': ['G', 'A']}

    transitions = 0
    transversions = 0

    for char1, char2 in zip(s1, s2):
        print(char1, char2)
        if transition_map[char1] == char2:
            transitions += 1
        if char2 in transversion_map[char1]:
            transversions +=1
    return (transitions / transversions)


s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
assert(round(transition_tranversion_ratio(s1, s2), 11) == 1.21428571429)


with open('data/rosalind_tran.txt', 'r') as f:
    records = [str(record.seq) for record in SeqIO.parse(f, 'fasta')]
    s1, s2 = records
    print(transition_tranversion_ratio(s1, s2))
