# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(ino, post):
            
            if len(ino) == 0:
                return None
            if len(ino) == 1:
                return TreeNode(ino[0])
            # print(post, ino)
            rootVal = post[-1]
            leftCount = ino.index(rootVal)
            
            root = TreeNode(rootVal)
            
            root.left = dfs(ino[:leftCount], post[:leftCount])
            root.right = dfs(ino[leftCount+1:], post[leftCount:-1])
            
            return root
        return dfs(inorder, postorder)