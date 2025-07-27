# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 
# mat[r][c] 的和： 
# 
#  
#  i - k <= r <= i + k, 
#  j - k <= c <= j + k 且 
#  (r, c) 在矩阵内。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n, k <= 100 
#  1 <= mat[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 前缀和 👍 216 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        perfix = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for r,row in enumerate(mat):
            for c,num in enumerate(row):
                perfix[r+1][c+1] = num + perfix[r][c+1] + perfix[r+1][c] - perfix[r][c]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                r1,r2 = max(0,r-k),min(len(mat)-1,r+k)
                c1,c2 = max(0,c-k),min(len(mat[0])-1,c+k)
                mat[r][c] = perfix[r2+1][c2+1] - perfix[r2+1][c1] - perfix[r1][c2+1] + perfix[r1][c1]
        return mat
# leetcode submit region end(Prohibit modification and deletion)
