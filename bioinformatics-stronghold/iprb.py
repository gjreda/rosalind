"""
Problem ID: IPRB
http://rosalind.info/problems/iprb/

Mendel's First Law
------------------
Given: Three positive integers k, m, and n, representing a population 
containing k+m+n organisms: k individuals are homozygous dominant for 
a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms 
will produce an individual possessing a dominant allele (and thus 
displaying the dominant phenotype). Assume that any two organisms can mate.
"""


def calculate_dominant_phenotype_probability(k, m, n):
    people = k + m + n
    if people < 2:
        raise ValueError

    p = 0

    # YY x (YY or Yy or yy) = 1.0
    p += (k / people) * ((k - 1) / (people - 1)) * 1.0
    p += (k / people) * (m / (people - 1)) * 1.0
    p += (k / people) * (n / (people - 1)) * 1.0

    # Yy x (YY or Yy or yy)
    p += (m / people) * (k / (people - 1)) * 1.0
    p += (m / people) * ((m - 1) / (people - 1)) * 0.75
    p += (m / people) * (n / (people - 1)) * 0.5

    # yy x (YY or Yy or yy)
    p += (n / people) * (k / (people - 1)) * 1.0
    p += (n / people) * (m / (people - 1)) * 0.5
    p += (n / people) * ((n - 1) / (people - 1)) * 0
    return p 

# test it
assert(calculate_dominant_phenotype_probability(2, 0, 0) == 1.0)
assert(calculate_dominant_phenotype_probability(1, 1, 0) == 1.0)
assert(calculate_dominant_phenotype_probability(1, 0, 1) == 1.0)
assert(calculate_dominant_phenotype_probability(0, 2, 0) == 0.75)
assert(calculate_dominant_phenotype_probability(0, 1, 1) == 0.5)
assert(calculate_dominant_phenotype_probability(0, 0, 2) == 0.0)
assert(round(calculate_dominant_phenotype_probability(2, 2, 2), 5) == 0.78333)

with open('data/rosalind_iprb.txt', 'r') as f:
    k, m, n = [int(s) for s in f.read().strip().split()]
    print(calculate_dominant_phenotype_probability(k, m, n))
