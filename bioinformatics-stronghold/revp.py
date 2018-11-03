"""
Locating Restriction Sites
http://rosalind.info/problems/revp/
"""

from typing import Dict
from Bio import SeqIO
from revc import reverse_complement


def is_reverse_palindrome(dna: str) -> bool:
    if dna == reverse_complement(dna):
        return True
    return False


def find_reverse_palindromes(dna: str,
                             minlen: int = 4,
                             maxlen: int = 12) -> Dict[int, int]:
    palindromes = {}

    for i in range(len(dna) - minlen + 1):
        for j in range(minlen, maxlen + 1):
            if i + j > len(dna):
                continue

            substring = dna[i:i+j]
            if is_reverse_palindrome(substring):
                print(i, j, substring, reverse_complement(substring))
                palindromes[i+1] = j
    return palindromes


# test it
dna = 'TCAATGCATGCGGGTCTATATGCAT'
expected = {4: 6, 5: 4, 6: 6, 7: 4, 17: 4,
            18: 4, 20: 6, 21: 4}
assert(find_reverse_palindromes(dna) == expected)


fout = open('data/answer.txt', 'w')
with open('data/rosalind_revp.txt', 'r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        dna = str(record.seq)
        palindromes = find_reverse_palindromes(dna)
        
        for k, v in palindromes.items():
            fout.write(f"{str(k)} {str(v)}\n")

fout.close()