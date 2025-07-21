# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 
# 
#  整数除法仅保留整数部分。 
# 
#  你可以假设给定的表达式总是有效的。所有中间结果将在 [-2³¹, 2³¹ - 1] 的范围内。 
# 
#  注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "3+2*2"
# 输出：7
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 3/2 "
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：s = " 3+5 / 2 "
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开 
#  s 表示一个 有效表达式 
#  表达式中的所有整数都是非负整数，且在范围 [0, 2³¹ - 1] 内 
#  题目数据保证答案是一个 32-bit 整数 
#  
# 
#  Related Topics 栈 数学 字符串 👍 847 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        opt = [1]
        i = 0
        num = ''
        while i < len(s):
            c = s[i]
            if c == '-':
                opt[-1] = -1
            elif c == '+':
                opt[-1]=1
            elif c == '*':
                opt[-1] = stack[-1]
            elif c == '/':
                opt[-1] = '/'
            elif c.isdigit():
                num += c
                if i+1 >= len(s) or not s[i+1].isdigit():
                    p = 1
                    while len(opt) > len(stack):
                        p *= opt.pop()
                    stack[-1] += opt[-1] * p*int(num)
                    num = ''
            i += 1
        return stack[-1]
# leetcode submit region end(Prohibit modification and deletion)
