# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def check_balanced(root):
            if not root: 
                return True, 0
            if (not root.left and not root.right):
                return True, 1
            l, r = 0, 0
            bal, l = check_balanced(root.left)
            bal2, r = check_balanced(root.right)
            if bal and bal2:
                if 0 <= abs(l-r) <= 1:
                    return True, max(l,r)+1
            return False, max(l,r)+1
        
        ans, h = check_balanced(root)
        return ans
        