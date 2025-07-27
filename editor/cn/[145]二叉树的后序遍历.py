# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。 
# 
#  
# 
#  示例 1： 
# 
#  
#  输入：root = [1,null,2,3] 
#  
# 
#  输出：[3,2,1] 
# 
#  解释： 
# 
#  
# 
#  示例 2： 
# 
#  
#  输入：root = [1,2,3,4,5,null,8,null,null,6,7,9] 
#  
# 
#  输出：[4,6,7,5,2,9,8,3,1] 
# 
#  解释： 
# 
#  
# 
#  示例 3： 
# 
#  
#  输入：root = [] 
#  
# 
#  输出：[] 
# 
#  示例 4： 
# 
#  
#  输入：root = [1] 
#  
# 
#  输出：[1] 
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 1242 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            if root.left:
                ans += self.postorderTraversal(root.left)
            if root.right:
                ans += self.postorderTraversal(root.right)
            ans.append(root.val)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
