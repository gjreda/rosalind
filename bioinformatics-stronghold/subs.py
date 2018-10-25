"""
Finding a Motif in DNA
http://rosalind.info/problems/subs/
"""


def find_substrings(s, t):
    positions = []
    search_len = len(t)
    for i in range(len(s)):
        if s[i:i+search_len] == t:
            positions.append(i + 1)
    return positions


# test it
s = 'GATATATGCATATACTT'
t = 'ATAT'
assert(find_substrings(s, t) == [2, 4, 10])


with open('data/rosalind_subs.txt', 'r') as f:
    lines = f.readlines()

s = lines[0].strip()
t = lines[1].strip()
answer = find_substrings(s, t)
print(' '.join(map(str, answer)))