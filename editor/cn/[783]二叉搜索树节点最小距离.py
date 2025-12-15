# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  差值是一个正数，其数值等于两值之差的绝对值。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
#  
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是 [2, 100] 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-
# bst/ 相同 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 二叉树 👍 304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        pre = float('-inf')

        def dfs(node):
            nonlocal res, pre
            if node:
                dfs(node.left)
                res = min(res, node.val - pre)
                pre = node.val
                dfs(node.right)

        dfs(root)
        return res
# leetcode submit region end(Prohibit modification and deletion)
