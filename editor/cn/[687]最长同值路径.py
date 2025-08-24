# 给定一个二叉树的
#  root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。 
# 
#  两个节点之间的路径长度 由它们之间的边数表示。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：root = [5,4,5,1,1,5]
# 输出：2
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入：root = [1,4,5,4,4,5]
# 输出：2
#  
# 
#  
# 
#  提示: 
# 
#  
#  树的节点数的范围是
#  [0, 10⁴] 
#  -1000 <= Node.val <= 1000 
#  树的深度将不超过 1000 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 838 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node,prev = -1):
            if node:
                nonlocal ans
                dep_l = dfs(node.left,node.val)
                dep_r = dfs(node.right,node.val)
                ans = max(ans, dep_r + dep_l)
                if node.val == prev:
                    return max(dep_r, dep_l) + 1
            return 0
        dfs(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
