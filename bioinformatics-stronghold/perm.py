"""
Enumerating Gene Orders
http://rosalind.info/problems/perm/
"""

from itertools import permutations

def perm_cheat(n):
    return list(permutations(range(1, n + 1)))

# because testing
def print_perms(perms):
    output = ''
    output += str(len(perms)) + '\n'
    for p in perms:
        output += ' '.join([str(n) for n in p]) + '\n'
    return output.strip()


testval = """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1"""

assert(print_perms(perm_cheat(3)) == testval)

with open('data/rosalind_perm.txt', 'r') as f:
    n = int(f.read())
    output = print_perms(perm_cheat(n))
    with open('data/answer.txt', 'w') as fw:
        fw.write(output)
