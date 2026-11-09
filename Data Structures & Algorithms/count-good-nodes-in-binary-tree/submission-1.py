# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def countgood(root, mx, count):
            if not root:
                return count
            # print(f"{count=}, {root.val=}, {mx=}")
            if not root.left and not root.right:
                if root.val >= mx:
                    count += 1
                return count
            if root.val >= mx:
                mx = root.val
                count += 1
            
            if root.left:
                count = countgood(root.left, mx, count)
            if root.right:
                count = countgood(root.right, mx, count)
            return count
        
        result = countgood(root, -101, 0)
        return result

        