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
        ans = []
        path = ['']*(n*2)
        def dfs(left,right):
            if right ==n:
                ans.append(''.join(path))
            if left < n:
                path[left+right]='('
                dfs(left+1,right)
            if right < left:
                path[left+right]=')'
                dfs(left,right+1)
        dfs(0,0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
