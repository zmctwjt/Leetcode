# 给你一个整数 n ，返回大于或等于 n 的最小 
#  
#  回文质数
#  。 
# 
# 
#  一个整数如果恰好有两个除数：1 和它本身，那么它是 质数 。注意，1 不是质数。 
# 
#  
#  例如，2、3、5、7、11 和 13 都是质数。 
#  
# 
#  一个整数如果从左向右读和从右向左读是相同的，那么它是 回文数 。 
# 
#  
#  例如，101 和 12321 都是回文数。 
#  
# 
#  测试用例保证答案总是存在，并且在 [2, 2 * 10⁸] 范围内。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 6
# 输出：7
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 8
# 输出：11
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 13
# 输出：101
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁸ 
#  
# 
#  Related Topics 数学 数论 👍 115 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from math import isqrt


class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(n):
            for i in range(2,isqrt(n)+1):
                if not n % i:
                    return False
            return n >1
        while not isPrime(n) or str(n) != str(n)[::-1]:
            n += 1
        return n
# leetcode submit region end(Prohibit modification and deletion)
