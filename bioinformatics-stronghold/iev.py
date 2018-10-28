"""
Calculating Expected Offspring
http://rosalind.info/problems/iev/
"""

def expected_offspring_dominant_phenotype(args):
    if len(args) != 6:
        raise ValueError
    p = 0
    p += args[0] * 1. * 2
    p += args[1] * 1. * 2
    p += args[2] * 1. * 2
    p += args[3] * .75 * 2
    p += args[4] * .5 * 2
    p += args[5] * 0 * 2
    return p

assert(expected_offspring_dominant_phenotype([1, 0, 0, 1, 0, 1]) == 3.5)

with open('data/rosalind_iev.txt') as f:
    args = [int(s) for s in f.read().strip().split()]
    print(expected_offspring_dominant_phenotype(args))