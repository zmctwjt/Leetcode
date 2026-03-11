# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。 
# 
#  请返回 封闭岛屿 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,
# 0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 335 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def dfs(row,col):
            if grid[row][col]:
                return True
            else:
                res = True
                grid[row][col] = 1
                for r,c in ((0,1),(1,0),(-1,0),(0,-1)):
                    if 0<= row+r<m and 0 <= col+c < n:
                        res &= dfs(row+r,col+c)
                    else:
                        res = False
                return res
        ans=0
        for r,row in enumerate(grid):
            for c,col in enumerate(row):
                if col == 0:
                    ans += int(dfs(r,c))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
