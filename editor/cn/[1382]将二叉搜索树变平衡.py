# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。 
# 
#  如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入: root = [2,1,3]
# 输出: [2,1,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树节点的数目在 [1, 10⁴] 范围内。 
#  1 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics 贪心 树 深度优先搜索 二叉搜索树 分治 二叉树 👍 237 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []
        def dfs(node):
            if node:
                dfs(node.left)
                vals.append(node.val)
                dfs(node.right)
        dfs(root)
        def create(l,r):
            if l<=r:
                mid = (l+r) // 2
                node = TreeNode(vals[mid])
                node.left = create(l,mid-1)
                node.right = create(mid+1,r)
                return node
        return create(0,len(vals)-1)
# leetcode submit region end(Prohibit modification and deletion)
