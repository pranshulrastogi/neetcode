# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def get_diam(root, ans):
            if not root:
                return 0, ans
            if not root.left and not root.right:
                return 1, max(1, ans)
            l, r = 0, 0
            if root.left:
                l, ans = get_diam(root.left, ans)
                # l += 1
            if root.right:
                r, ans = get_diam(root.right, ans)
            ans = max(ans, l+r)
            if l > r:
                return l+1, ans
            else:
                return r+1, ans
        if not root or not root.left and not root.right:
            return 0
        d, ans = get_diam(root, 0)
        return ans
        