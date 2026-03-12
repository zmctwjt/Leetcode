# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。. 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树的节点数在 [0, 5000] 范围内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 排序 👍 191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        res1 = []
        res2 = []
        def dfs(node,res):
            if node:
                dfs(node.left,res)
                res.append(node.val)
                dfs(node.right,res)
        dfs(root2,res2)
        dfs(root1,res1)
        l,r = 0,0
        res = []
        while l<len(res1) or r<len(res2):
            if l < len(res1):
                if r < len(res2):
                    if res1[l] <= res2[r]:
                        res.append(res1[l])
                        l +=1
                    else:
                        res.append(res2[r])
                        r +=1
                else:
                    res.append(res1[l])
                    l += 1
            else:
                res.append(res2[r])
                r += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
