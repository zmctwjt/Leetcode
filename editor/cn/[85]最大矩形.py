# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  1 <= rows, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
# 
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1803 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
