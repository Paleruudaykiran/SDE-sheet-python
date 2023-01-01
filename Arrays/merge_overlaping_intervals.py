from sys import stdin
class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    intervals = sorted(intervals,key = lambda x : [x.start,x.end]) 
    mintervals = [] 
    mintervals.append(intervals[0])
    for i in range(1,len(intervals)) :
        prev = mintervals[-1]
        if prev.end <= intervals[i].end and prev.end >= intervals[i].start:
            prev.end = intervals[i].end 
        else : 
            mintervals.append(intervals[i]) 
    for x in mintervals : 
        print(x.start,x.end)
    return mintervals
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)
mergeIntervals(intervals)