from os import *
from sys import *
from collections import *
from math import *

'''
# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

def verticalOrderTraversal(root):
    d = {}
    q = deque()
    q.append([root,0])
    while len(q) > 0 :
        node,col = q.popleft() 
        if col in d.keys() :
            d[col].append(node.data) 
        else :
            d[col] = [node.data] 
        
        if node.left :
            q.append([node.left,col-1]) 
        if node.right :
            q.append([node.right,col+1]) 
    lis = list(d.items())
    lis = sorted(d.items(),key=lambda x:x[0]) 
    for x in lis :
        print(*x[1],end=" ") 
    return []
