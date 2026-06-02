# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10ⁿ 。
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
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。 
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：1
#  
# 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 8 
#  
# 
#  Related Topics 数学 动态规划 回溯 👍 373 👎 0
from functools import reduce


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 0
        for i in range(n):
            t = 9
            for j in range(9,9-i,-1):
                t *= j
            ans += t
        return ans+1
# leetcode submit region end(Prohibit modification and deletion)
