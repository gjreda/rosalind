"""
Overlap Graphs
http://rosalind.info/problems/grph/
"""

from Bio import SeqIO
from typing import Dict, List, Tuple
from collections import defaultdict
from io import StringIO


def create_overlap_graph(filehandler: str, k: int) -> List[Tuple[str, str]]:
    overlap_graph = []
    prefix_map = defaultdict(list)
    suffix_map = defaultdict(list)

    # scan through file to create prefix and suffix indexes
    for record in SeqIO.parse(filehandler, 'fasta'):
        dna = str(record.seq)
        prefix = dna[:k]
        suffix = dna[-k:]

        prefix_map[prefix].append(record.id)
        suffix_map[suffix].append(record.id)

    # find prefix-suffix overlap: 
    # these are the only items with possible overlapping sequences
    # also, this block is not pretty
    overlap = set(prefix_map.keys()).intersection(set(suffix_map.keys()))
    for substr in overlap:
        for prefix_id in prefix_map[substr]:
            for suffix_id in suffix_map[substr]:
                if prefix_id != suffix_id:
                    overlap_graph.append((suffix_id, prefix_id))
    return overlap_graph


filehandler = StringIO(""">Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG""")

expected = [
    ('Rosalind_0498', 'Rosalind_2391'),
    ('Rosalind_0498', 'Rosalind_0442'),
    ('Rosalind_2391', 'Rosalind_2323')
]
assert(sorted(create_overlap_graph(filehandler, k=3)) == sorted(expected))



with open('data/rosalind_grph.txt', 'r') as f:
    overlap = create_overlap_graph(f, k=3)

with open('data/answer.txt', 'w') as f:
    for edge in overlap:
        f.write(f"{edge[0]} {edge[1]}\n")