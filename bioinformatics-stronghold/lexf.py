"""
Enumerating k-mers Lexicographically
http://rosalind.info/problems/lexf/
"""

from typing import List
import itertools

def ordered_strings(letters: str, length: int) -> List[str]:
    chars = ''.join(sorted(letters.replace(' ', '')))
    combos = []
    for item in itertools.product(chars, repeat=length):
        combos.append(''.join(item))
    return sorted(combos)


expected = ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 
            'CG', 'CT', 'GA', 'GC', 'GG', 'GT',
            'TA', 'TC', 'TG', 'TT']
assert(ordered_strings('A C G T', 2) == expected)


with open('data/rosalind_lexf.txt') as f:
    letters, length = f.read().strip().split('\n')

print(letters, length)
results = ordered_strings(letters, int(length))
for line in results:
    print(line)