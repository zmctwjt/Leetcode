# 给出一个字符串 s（仅含有小写英文字母和括号）。 
# 
#  请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。 
# 
#  注意，您的结果中 不应 包含任何括号。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "(abcd)"
# 输出："dcba"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 解释：先反转子字符串 "love" ，然后反转整个字符串。 
# 
#  示例 3： 
# 
#  
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 中只有小写英文字母和括号 
#  题目测试用例确保所有括号都是成对出现的 
#  
# 
#  Related Topics 栈 字符串 👍 308 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(self, s):
        # stack = []
        # temp = ''
        # for c in s:
        #     if c == ')':
        #         if stack:
        #             temp =stack.pop() + temp[::-1]
        #     elif c == '(':
        #         stack.append(temp)
        #         temp = ''
        #     else:
        #         temp += c
        # return temp
        stack,cnt = [],{}
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                t = stack.pop()
                cnt[t],cnt[i] = i,t
        i = 0
        step = 1
        while 0<=i<len(s):
            c = s[i]
            if not c.isalpha():
                i = cnt[i]
                step = -step
            else:
                stack.append(c)
            i += step
        return ''.join(stack)

# leetcode submit region end(Prohibit modification and deletion)
