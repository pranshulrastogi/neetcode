# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = []
        if not root:
            return q
        q = [root, "$"]
        ans = []
        prev = None
        while q:
            n = q.pop(0)
            if n == "$":
                ans.append(prev)
                if q:
                    q.append("$")
            else:
                prev = n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return ans
                

        