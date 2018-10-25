"""
Problem ID: REVC
http://rosalind.info/problems/revc/

Complementing a Strand of DNA
"""

def reverse_complement(s):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_ = s.strip()[::-1]
    
    complement = ''
    for letter in reversed_:
        complement += pairs[letter]
    return complement


s = 'AAAACCCGGT'
assert(reverse_complement(s) == 'ACCGGGTTTT')


with open('data/rosalind_revc.txt', 'r') as f:
    print(reverse_complement(f.read()))