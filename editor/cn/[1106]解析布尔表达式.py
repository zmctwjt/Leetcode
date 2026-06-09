# 布尔表达式 是计算结果不是 true 就是 false 的表达式。有效的表达式需遵循以下约定： 
# 
#  
#  't'，运算结果为 true 
#  'f'，运算结果为 false 
#  '!(subExpr)'，运算过程为对内部表达式 subExpr 进行 逻辑非（NOT）运算 
#  '&(subExpr1, subExpr2, ..., subExprn)'，运算过程为对 2 个或以上内部表达式 subExpr1, subExpr2,
#  ..., subExprn 进行 逻辑与（AND）运算 
#  '|(subExpr1, subExpr2, ..., subExprn)'，运算过程为对 2 个或以上内部表达式 subExpr1, subExpr2,
#  ..., subExprn 进行 逻辑或（OR）运算 
#  
# 
#  给你一个以字符串形式表述的 布尔表达式 expression，返回该式的运算结果。 
# 
#  题目测试用例所给出的表达式均为有效的布尔表达式，遵循上述约定。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：expression = "&(|(f))"
# 输出：false
# 解释：
# 首先，计算 |(f) --> f ，表达式变为 "&(f)" 。
# 接着，计算 &(f) --> f ，表达式变为 "f" 。
# 最后，返回 false 。
#  
# 
#  示例 2： 
# 
#  
# 输入：expression = "|(f,f,f,t)"
# 输出：true
# 解释：计算 (false OR false OR false OR true) ，结果为 true 。
#  
# 
#  示例 3： 
# 
#  
# 输入：expression = "!(&(f,t))"
# 输出：true
# 解释：
# 首先，计算 &(f,t) --> (false AND true) --> false --> f ，表达式变为 "!(f)" 。
# 接着，计算 !(f) --> NOT false --> true ，返回 true 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= expression.length <= 2 * 10⁴ 
#  expression[i] 为 '('、')'、'&'、'|'、'!'、't'、'f' 和 ',' 之一 
#  
# 
#  Related Topics 栈 递归 字符串 👍 217 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def p(opt,a,b):
            if opt == '&':
                return a and b
            else:
                return a or b

        def dfs(i,opt):
            ans = None
            while expression[i] != ')':
                if expression[i] in '!&|':
                    t,j = dfs(i+2,expression[i])
                    if ans == None:
                        ans = t
                    ans = not t if opt == '!' else p(opt,ans,t)
                    i = j
                elif expression[i] == 'f':
                    if ans == None:
                        ans =False
                    ans = True if opt == '!' else p(opt,ans,False)
                elif expression[i] == 't':
                    if ans == None:
                        ans = True
                    ans = False if opt == '!' else p(opt,ans,True)
                i += 1
            return ans,i
        if expression == 't':
            return True
        elif expression == 'f':
            return False
        else:
            return dfs(2,expression[0])[0]

# leetcode submit region end(Prohibit modification and deletion)
