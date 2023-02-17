from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
def gen(root,lis) :
    if root != None :
        lis[1].append(root.data) 
        gen(root.left,lis)  
        lis[0].append(root.data) 
        gen(root.right,lis)  
        lis[2].append(root.data) 
def getTreeTraversal(root):
    lis = [[],[],[]] 
    gen(root,lis) 
    return lis