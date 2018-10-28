"""
Problem ID: FIB
http://rosalind.info/problems/fib/

Rabbits and Recurrence Relations
"""


def recursive_rabbits(n: int, k: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return recursive_rabbits(n - 1, k) + (recursive_rabbits(n - 2, k) * k)


n = 5
k = 3
assert(recursive_rabbits(n, k) == 19)


with open('data/rosalind_fib.txt', 'r') as f:
    n, k = map(int, f.read().split())
    print(recursive_rabbits(n, k))