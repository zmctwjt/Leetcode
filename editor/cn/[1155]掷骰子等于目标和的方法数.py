# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。 
# 
#  给定三个整数 n、k 和 target，请返回投掷骰子的所有可能得到的结果（共有 kⁿ 种方式），使得骰子面朝上的数字总和等于 target。 
# 
#  由于答案可能很大，你需要对 10⁹ + 7 取模。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1, k = 6, target = 3
# 输出：1
# 解释：你掷了一个有 6 个面的骰子。
# 得到总和为 3 的结果的方式只有一种。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你掷了两个骰子，每个骰子有 6 个面。
# 有 6 种方式得到总和为 7 的结果: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 30, k = 30, target = 500
# 输出：222616187
# 解释：返回的结果必须对 10⁹ + 7 取模。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n, k <= 30 
#  1 <= target <= 1000 
#  
# 
#  Related Topics 动态规划 👍 318 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
MOD = 10**9+7
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(n)]
        for i in range(n):
            for j in range(i+1,target+1):
                for t in range(1,min(j,k)):
                    dp[i][j] += dp[i][j-t]
        return dp[-1][-1] % MOD
# leetcode submit region end(Prohibit modification and deletion)
