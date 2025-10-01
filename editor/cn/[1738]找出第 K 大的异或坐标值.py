# 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。 
# 
#  矩阵中坐标 (a, b) 的 目标值 可以通过对所有元素 matrix[i][j] 执行异或运算得到，其中 i 和 j 满足 0 <= i <= a < 
# m 且 0 <= j <= b < n（下标从 0 开始计数）。 
# 
#  请你找出 matrix 的所有坐标中第 k 大的目标值（k 的值从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[5,2],[1,6]], k = 1
# 输出：7
# 解释：坐标 (0,1) 的目标值是 5 XOR 2 = 7 ，为最大的目标值。 
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[5,2],[1,6]], k = 2
# 输出：5
# 解释：坐标 (0,0) 的目标值是 5 = 5 ，为第 2 大的目标值。 
# 
#  示例 3： 
# 
#  
# 输入：matrix = [[5,2],[1,6]], k = 3
# 输出：4
# 解释：坐标 (1,0) 的目标值是 5 XOR 1 = 4 ，为第 3 大的目标值。 
# 
#  示例 4： 
# 
#  
# 输入：matrix = [[5,2],[1,6]], k = 4
# 输出：0
# 解释：坐标 (1,1) 的目标值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的目标值。 
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 1000 
#  0 <= matrix[i][j] <= 10⁶ 
#  1 <= k <= m * n 
#  
# 
#  Related Topics 位运算 数组 分治 矩阵 前缀和 快速选择 排序 堆（优先队列） 👍 135 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        perfix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        ans = []
        for r,row in enumerate(matrix):
            for c,val in enumerate(row):
                perfix[r+1][c+1] = val^perfix[r+1][c]^perfix[r][c+1]^perfix[r][c]
                ans.append(perfix[r+1][c+1])
        return sorted(ans)[-k]
# leetcode submit region end(Prohibit modification and deletion)
