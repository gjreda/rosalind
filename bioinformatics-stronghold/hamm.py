"""
Problem ID: HAMM
http://rosalind.info/problems/hamm/

Counting Point Mutations
"""


def hamming_distance(s, t):
    distance = 0
    for char_s, char_t in zip(s, t):
        if char_s != char_t:
            distance += 1
    return distance


# test it
s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
assert(hamming_distance(s, t) == 7)


with open('data/rosalind_hamm.txt', 'r') as f:
    lines = [line for line in f]

distance = hamming_distance(lines[0], lines[1])
print(f"Hamming Distance = {distance}")