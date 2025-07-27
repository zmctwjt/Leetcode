# 给定两个整数 a 和 b ，返回 任意 字符串 s ，要求满足： 
# 
#  
#  s 的长度为 a + b，且正好包含 a 个 'a' 字母与 b 个 'b' 字母； 
#  子串 'aaa' 没有出现在 s 中； 
#  子串 'bbb' 没有出现在 s 中。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：a = 1, b = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：a = 4, b = 1
# 输出："aabaa" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= a, b <= 100 
#  对于给定的 a 和 b，保证存在满足要求的 s 
#  
# 
# 
#  Related Topics 贪心 字符串 👍 102 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        if a >= b:
            if a >= 2:
                ans.append('a'*2)
            else:
                ans.append('a'*a)



        
# leetcode submit region end(Prohibit modification and deletion)
