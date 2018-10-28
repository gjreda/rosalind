"""
Computing GC Content
http://rosalind.info/problems/gc/
"""

from Bio import SeqIO
from io import StringIO


def calculate_gc_content(dna: str) -> float:
    amount = 0
    for char in dna:
        if char in ('G', 'C'):
            amount += 1
    return (amount / len(dna)) * 100


def get_max_gc(contents: dict) -> str:
    return max(contents, key=contents.get)


if __name__ == '__main__':
    contents = {}
    with open('data/rosalind_gc.txt', 'r') as f:
        for record in SeqIO.parse(f, 'fasta'):
            sequence = str(record.seq)
            contents[record.id] = calculate_gc_content(sequence)
    
    max_gc = get_max_gc(contents)
    print(max_gc)
    print(contents[max_gc])