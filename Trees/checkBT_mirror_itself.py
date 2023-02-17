'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def check(self,root) :
        if root == None :
            return 
        root.left,root.right = root.right,root.left 
        self.check(root.left) 
        self.check(root.right)
    def mirror(self,root):
        self.check(root)
