from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):
  if root == None :
    return 0
  q = deque() 
  q.append(root) 
  ans = 1
  while len(q) > 0 :
    n = len(q)
    if n > ans :
      ans = n 
    #print(n)
    for i in range(n) :
      node = q.popleft() 
      if node.left :
        q.append(node.left) 
      if node.right : 
        q.append(node.right) 
  return ans

