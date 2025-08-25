# 给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色
# 。 
# 
#  如果两个方块在任意 4 个方向上相邻，则称它们 相邻 。 
# 
#  如果两个方块具有相同的颜色且相邻，它们则属于同一个 连通分量 。 
# 
#  连通分量的边界 是指连通分量中满足下述条件之一的所有网格块： 
# 
#  
#  在上、下、左、右任意一个方向上与不属于同一连通分量的网格块相邻 
#  在网格的边界上（第一行/列或最后一行/列） 
#  
# 
#  请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色。 
# 
#  并返回最终的网格 grid 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# 输出：[[3,3],[3,2]] 
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# 输出：[[1,3,3],[2,3,3]] 
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# 输出：[[2,2,2],[2,1,2],[2,2,2]] 
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  1 <= grid[i][j], color <= 1000 
#  0 <= row < m 
#  0 <= col < n 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 190 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        def dfs(row,col,cur,tag):
            if any(r<0 or r==m or c<0 or c==n or (grid[r][c]!=cur and grid[r][c]!=tag)  for r,c in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]):


        dfs(row,col,grid[row][col],color)
        return grid

# leetcode submit region end(Prohibit modification and deletion)
