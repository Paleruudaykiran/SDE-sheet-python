'''
	Time Complexity: O(N^2 * log(N))
	Space complexity: O(N^2)

	Where 'N' is the number of element present in the given array.
'''

from operator import attrgetter
from collections import namedtuple

pair = namedtuple('pair', ['sum', 'id1', 'id2'])

def commanid(p1, p2):
    return p1.id1 == p2.id1 or p1.id1 == p2.id2 or p1.id2 == p2.id1 or p1.id2 == p2.id2

def fourSum(a, target):
    seq = []
    flag = False
    n = len(a)

    for i in range(n - 1):
        for j in range(i + 1, n):
            p = pair(a[i] + a[j], i, j)
            seq.append(p)

    size = len(seq)
    seq = sorted(seq, key=attrgetter('sum'))
    left = 0
    right = size - 1

    while left < size and right >= 0:
        Sum = seq[left].sum + seq[right].sum
        
        if Sum == target and not commanid(seq[left], seq[right]):
            return "Yes"
            flag = True
            break

        elif Sum < target:
            left += 1

        else:
            right -= 1
            

    return "No"