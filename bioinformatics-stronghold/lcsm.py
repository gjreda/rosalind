"""
Problem ID: LCSM
http://rosalind.info/problems/lcsm/

Trying to write this in a way that is cognizant of memory.
"""

from io import StringIO
from Bio import SeqIO

# TODO improvements:
# - Given a found match of len Y, only check for match > Y going forward
# - Also probably smarter to find longest length first and count backwards


def find_matches(a, b, minlength=2):
    """Find the longest shared substring within two given strings.

    Params
    ------
    a : str
    b : str

    Returns
    -------
    str
    """
    matches = set()
    for i in range(len(a)):
        for j in range(minlength, len(a)):
            if j - i < minlength:
                continue

            substring = a[i:j] 
            if substring in b:
                matches.add(substring)
    return matches


def find_shared_motif(filehandler):
    match_list = []

    for i, record in enumerate(SeqIO.parse(filehandler, 'fasta')):
        if i == 0:
            dnaseq = str(record.seq)

        found = find_matches(dnaseq, str(record.seq), minlength=2)
        match_list.append(found)  # list of match sets

    shared = set.intersection(*match_list)  # matches across all sets
    return sorted(shared, key=len, reverse=True)[0]


filehandler = StringIO(""">Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
""")

assert(find_shared_motif(filehandler) == 'AC')

with open('data/rosalind_lcsm.txt', 'r') as f:
    print(find_shared_motif(f))