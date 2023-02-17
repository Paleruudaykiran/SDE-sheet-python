# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def gen(self,root,tar,lis) :
        if root == None :
            return 0 
        lis.append(root.val)
        if root.val == tar :
            return 1 
        if self.gen(root.left,tar,lis) or self.gen(root.right,tar,lis) :
            return 1 
        lis.pop()
        return 0
        
            
    def solve(self, A, B):
        lis = [] 
        self.gen(A,B,lis) 
        return lis