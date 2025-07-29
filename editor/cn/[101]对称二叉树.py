# 给你一个二叉树的根节点 root ， 检查它是否轴对称。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 2984 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if left and right:
                return dfs(left.left,right.right) and dfs(left.right,right.left) and left.val == right.val
            elif (not left) ^ (not right):
                return False
            return True
        return dfs(root.left,root.right)
# leetcode submit region end(Prohibit modification and deletion)
