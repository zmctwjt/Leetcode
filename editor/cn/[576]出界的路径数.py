# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以
# 穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。 
# 
#  给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 
# 10⁹ + 7 取余 后的结果。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# 输出：6
#  
# 
#  示例 2： 
#  
#  
# 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 50 
#  0 <= maxMove <= 50 
#  0 <= startRow < m 
#  0 <= startColumn < n 
#  
# 
#  Related Topics 动态规划 👍 329 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        if maxMove == 0:
            return 0

        # 初始化前一步的状态
        prev_dp = [[0] * n for _ in range(m)]
        prev_dp[startRow][startColumn] = 1  # 初始位置
        result = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in range(1, maxMove + 1):
            curr_dp = [[0] * n for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    if prev_dp[row][col] == 0:
                        continue  # 优化：跳过无路径的位置
                    # 遍历四个方向
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            # 未出界：累加到新位置
                            curr_dp[nr][nc] = (curr_dp[nr][nc] + prev_dp[row][col]) % MOD
                        else:
                            # 出界：累加到结果
                            result = (result + prev_dp[row][col]) % MOD
            prev_dp = curr_dp  # 更新状态

        return result

# leetcode submit region end(Prohibit modification and deletion)
