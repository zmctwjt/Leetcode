# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 3983 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        def dfs(i,left):
            if i == 2*n:
                if left == 0:
                    ans.append(''.join(path))
                return
            if left < n:
                path.append('(')
                dfs(i+1,left+1)
                path.pop()
            if left:
                path.append(')')
                dfs(i+1,left-1)
                path.pop()
        dfs(0,0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
