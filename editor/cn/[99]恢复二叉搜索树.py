# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。 
# 
#  
# 
#  提示： 
# 
#  
#  树上节点的数目在范围 [2, 1000] 内 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  
# 
#  进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？ 
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 1033 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        x = None
        y = None
        def dfs(node):
            nonlocal pre, x, y
            if node:
                dfs(node.left)
                if pre and pre.val > node.val:
                    if x:
                        y = node
                        return
                    else:
                        x = pre
                pre = node
                dfs(node.right)
        dfs(root)
        x.val,y.val = y.val,x.val
# leetcode submit region end(Prohibit modification and deletion)
