# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 10⁴ 
#  1 <= m * n <= 10⁴ 
#  mat[i][j] is either 0 or 1. 
#  mat 中至少有一个 0 
#  
# 
#  Related Topics 广度优先搜索 数组 动态规划 矩阵 👍 1003 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        q = [([(r,c)],1) for r,row in enumerate(mat) for c,col in enumerate(row) if col == 1]
        for item in q:
            r,c = item[0][-1]
            step = item[1]
            mat[r][c] = -1
            for dr,dc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0 <= dr < m and 0 <= dc < n
                    if not mat[dr][dc]:
                        for r,c in item[0]:
                            if mat[r][c] == -1:
                                mat[r][c] = step
                            step -= 1
                    elif mat[dr][dc]!=-1:



# leetcode submit region end(Prohibit modification and deletion)

