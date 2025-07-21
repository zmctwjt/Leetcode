# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 
# 
#  注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "1 + 1"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 2-1 + 2 "
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由数字、'+'、'-'、'('、')'、和 ' ' 组成 
#  s 表示一个有效的表达式 
#  '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效) 
#  '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的) 
#  输入中不存在两个连续的操作符 
#  每个数字和运行的计算将适合于一个有符号的 32位 整数 
#  
# 
#  Related Topics 栈 递归 数学 字符串 👍 1137 👎 0


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
            elif c.isdigit():
                num += c
                if i+1 >= len(s) or not s[i+1].isdigit():
                    p = 1
                    while len(opt) > len(stack):
                        p *= opt.pop()
                    stack[-1] += opt[-1] * p*int(num)
                    num = ''
            elif c=='(':
                stack.append(0)
                opt.append(1)
            elif c==')':
                temp = stack.pop()
                opt.pop()
                stack[-1] += temp*opt[-1]
            i += 1
        return stack[-1]





# leetcode submit region end(Prohibit modification and deletion)
