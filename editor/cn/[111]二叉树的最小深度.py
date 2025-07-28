# 给定一个二叉树，找出其最小深度。
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明：叶子节点是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的范围在 [0, 10⁵] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs(node, depth=0):
        #     if node.left and node.right:
        #         return min(dfs(node.left, depth), dfs(node.right, depth)) +1
        #     elif node.left:
        #         return dfs(node.left, depth) +1
        #     elif node.right:
        #         return dfs(node.right, depth) +1
        #     else:
        #         return depth + 1
        # return dfs(root) if root else 0
        if root:
            q = deque([(root,1)])
            while q:
                node,depth = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append((node.left,depth+1))
                if node.right:
                    q.append((node.right,depth+1))
        return 0

# leetcode submit region end(Prohibit modification and deletion)
