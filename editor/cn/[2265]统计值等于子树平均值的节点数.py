# 给你一棵二叉树的根节点 root ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。 
# 
#  注意： 
# 
#  
#  n 个元素的平均值可以由 n 个元素 求和 然后再除以 n ，并 向下舍入 到最近的整数。 
#  root 的 子树 由 root 和它的所有后代组成。 
#  
# 
#  
# 
#  示例 1： 
#  输入：root = [4,8,5,0,1,null,6]
# 输出：5
# 解释：
# 对值为 4 的节点：子树的平均值 (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 。
# 对值为 5 的节点：子树的平均值 (5 + 6) / 2 = 11 / 2 = 5 。
# 对值为 0 的节点：子树的平均值 0 / 1 = 0 。
# 对值为 1 的节点：子树的平均值 1 / 1 = 1 。
# 对值为 6 的节点：子树的平均值 6 / 1 = 6 。
#  
# 
#  示例 2： 
#  输入：root = [1]
# 输出：1
# 解释：对值为 1 的节点：子树的平均值 1 / 1 = 1。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  0 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 50 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if node:
                left_sum,left_num =dfs(node.left)
                right_sum,right_num = dfs(node.right)
                sum_ = left_sum+right_sum+node.val
                num = left_num+right_num+1
                ans += sum_ // num == node.val
                return sum_,num
            return 0 , 0
        dfs(root)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)
