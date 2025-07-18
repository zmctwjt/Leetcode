# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数： 
# 
#  
#  () 得 1 分。 
#  AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。 
#  (A) 得 2 * A 分，其中 A 是平衡括号字符串。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入： "()"
# 输出： 1
#  
# 
#  示例 2： 
# 
#  输入： "(())"
# 输出： 2
#  
# 
#  示例 3： 
# 
#  输入： "()()"
# 输出： 2
#  
# 
#  示例 4： 
# 
#  输入： "(()(()))"
# 输出： 6
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 是平衡括号字符串，且只含有 ( 和 ) 。 
#  2 <= S.length <= 50 
#  
# 
#  Related Topics 栈 字符串 👍 543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i,c in enumerate(s):
            if stack and c == ')':
                j,score = stack.pop()
                if i-j == 1:
                    score += 1
                else:
                    score*= 2
                if stack:
                    stack[-1][1] += score
                else:
                    ans += score
            else:
                stack.append([i,0])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
