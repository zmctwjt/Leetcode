# 「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 `grid`，字符串中仅包含 `"0"～"5"` 这 6 个字符。地
# 图上每一个字符代表面积为 1 的区域，其中 `"0"` 表示走廊，其他字符表示主题空间。相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。
# 
# 
# 假如整个 `grid` 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 `0`。
# 
# **示例 1：**
# 
# > 输入：`grid = ["110","231","221"]`
# >
# > 输出：`1`
# >
# > 解释：4 个主题空间中，只有 1 个不与走廊相邻，面积为 1。
# > ![image.png](https://pic.leetcode-cn.com/1613708145-rscctN-image.png)
# 
# **示例 2：**
# 
# > 输入：`grid = ["11111100000","21243101111","21224101221","11111101111"]`
# >
# > 输出：`3`
# >
# > 解释：8 个主题空间中，有 5 个不与走廊相邻，面积分别为 3、1、1、1、2，最大面积为 3。
# > ![image.png](https://pic.leetcode-cn.com/1613707985-KJyiXJ-image.png)
# 
# **提示：**
# - `1 <= grid.length <= 500`
# - `1 <= grid[i].length <= 500`
# - `grid[i][j]` 仅可能为 `"0"～"5"`
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 28 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        m,n=len(grid),len(grid[0])
        visited = set()
        def dfs(r,c,v):
            if 0<=r<m and 0<=c<n and (grid[r][c]==v or v=='0') and (r,c) not in visited:
                visited.add((r,c))
                v = grid[r][c]
                return 1+dfs(r+1,c,v)+dfs(r-1,c,v)+dfs(r,c+1,v)+dfs(r,c-1,v)
            return 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='0' or r in (0,m-1) or c in (0,n-1):
                    dfs(r,c,grid[r][c])
        ans = 0
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited:
                    ans = max(dfs(r,c,grid[r][c]),ans)
        return ans
# leetcode submit region end(Prohibit modification and deletion)

