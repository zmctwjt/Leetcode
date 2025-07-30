# 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。 
# 
#  由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6]
# 输出：110
# 解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,null,2,3,4,null,null,5,6]
# 输出：90
# 解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
#  
# 
#  示例 3： 
# 
#  输入：root = [2,3,9,10,7,8,6,5,4,11,1]
# 输出：1025
#  
# 
#  示例 4： 
# 
#  输入：root = [1,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 50000 个节点，且至少有 2 个节点。 
#  每个节点的值在 [1, 10000] 之间。 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 122 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MOD = 10 ** 9 + 7
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sumTree(node):
            if node:
                return sumTree(node.left) + sumTree(node.right) + node.val
            return 0
        sum_ = sumTree(root)
        ans = 0
        def dfs(node):
            nonlocal ans
            if node:
                cur_sum = dfs(node.left) + dfs(node.right) + node.val
                ans = max(ans,cur_sum*(sum_-cur_sum))
                return cur_sum
            return 0
        dfs(root)
        return ans%MOD

# leetcode submit region end(Prohibit modification and deletion)
