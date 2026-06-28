# 给你三个正整数 a、b 和 c。 
# 
#  你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算 a OR b == c 成立的最小翻转次数。 
# 
#  「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：a = 2, b = 6, c = 5
# 输出：3
# 解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c 
# 
#  示例 2： 
# 
#  输入：a = 4, b = 2, c = 7
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：a = 1, b = 2, c = 3
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a <= 10^9 
#  1 <= b <= 10^9 
#  1 <= c <= 10^9 
#  
# 
#  Related Topics 位运算 👍 93 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1
            if c_bit:
                ans += 0 if a_bit | b_bit else 1
            else:
                ans +=a_bit+b_bit if a_bit | b_bit else 0
            a >>= 1
            b >>= 1
            c >>= 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
