# 给你二叉树的根节点 root ，请你采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。 
# 
#  空节点使用一对空括号对 "()" 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4]
# 输出："1(2(4))(3)"
# 解释：初步转化后得到 "1(2(4)())(3()())" ，但省略所有不必要的空括号对后，字符串应该是"1(2(4))(3)" 。
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,3,null,4]
# 输出："1(2()(4))(3)"
# 解释：和第一个示例类似，但是无法省略第一个空括号对，否则会破坏输入与输出一一映射的关系。 
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是 [1, 10⁴] 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 字符串 二叉树 👍 413 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            left,right = self.tree2str(root.left),self.tree2str(root.right)
            if right and not left:
                return f'{root.val}()({right})'
            return f'{root.val}{left and f"({left})"}{right and f"({right})"}'
        return ''
# leetcode submit region end(Prohibit modification and deletion)
