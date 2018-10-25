"""
Problem ID: DNA
http://rosalind.info/problems/dna/

Counting DNA Nucleotides
"""
from collections import Counter

def count_dna_nucleotides(s):
    try:
        letters = s.strip()
    except AttributeError as e:
        raise AttributeError('Function `count_dna_nucleotides` expects a str')

    counts = Counter(letters)
    return '{} {} {} {}'.format(counts['A'], counts['C'],
                                counts['G'], counts['T'])


s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
assert(count_dna_nucleotides(s) == '20 12 17 21')


with open('data/rosalind_dna.txt', 'r') as f:
    print(count_dna_nucleotides(f.read()))