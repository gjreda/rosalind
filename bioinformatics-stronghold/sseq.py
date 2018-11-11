"""
Finding a Spliced Motif
http://rosalind.info/problems/sseq/
"""

from Bio import SeqIO
from typing import List


def _add1(some_list):
    return [x + 1 for x in some_list]

def find_subsequences(s: str,
                      t: str,
                      s_position: int = 0,
                      t_position: int = 0,
                      subsequences: List[int] = []) -> List[int]:
    for i in range(s_position, len(s) + 1):
        if len(t) == len(subsequences):
            # return if we have a full subsequence
            return _add1(subsequences)  # rosalind wants 1-based indices

        if s[i] == t[t_position]:
            subsequences.append(i)

            s_position = i + 1
            t_position += 1
            find_subsequences(s, t, s_position, t_position,
                                subsequences=subsequences)
    return  # handle in case we don't find anything


assert(find_subsequences('ACGTACGTGACG', 'GTA', subsequences=[]) == [3, 4, 5])
assert(find_subsequences('TATGCTAAGATC', 'ACG', subsequences=[]) == [2, 5, 9])


with open('data/rosalind_sseq.txt') as f:
    records = [str(record.seq) for record in SeqIO.parse(f, 'fasta')]

s, t = records
subsequences = find_subsequences(s, t)
print(' '.join(map(str, subsequences)))
