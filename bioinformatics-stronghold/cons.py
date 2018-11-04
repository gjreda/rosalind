"""
Consensus and Profile
http://rosalind.info/problems/cons/
"""

from Bio import SeqIO
from collections import Counter, defaultdict


class Pileup(object):
    def __init__(self):
        self.pileup = []

    def read(self, filehandler):
        with open(filehandler, 'r') as f:
            counter = defaultdict(Counter)

            for read in SeqIO.parse(f, 'fasta'):
                dna = str(read.seq)
                self.pileup.append(list(dna))

                for i in range(len(dna)):
                    counter[i].update(dna[i])

        consensus = ''
        profile = defaultdict(list)
        for idx, counts in counter.items():
            consensus += counts.most_common(1)[0][0]

            for base in ('A', 'C', 'G', 'T'):
                profile[base].append(counter[idx].get(base, 0))

        self.consensus = consensus
        self._profile = profile

    @property
    def profile(self):
        for k, v in self._profile.items():
            print(f"{k}: {' '.join(map(str, v))}")


if __name__ == '__main__':
    pileup = Pileup()
    pileup.read('data/rosalind_cons.txt')
    print(pileup.consensus)
    pileup.profile