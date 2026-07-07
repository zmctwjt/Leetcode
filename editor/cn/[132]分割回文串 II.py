# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。 
# 
#  返回符合要求的 最少分割次数 。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 864 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[True]*n for _ in range(n)]
        for r in range(1, n):
            for l in range(r):
                is_palindrome[l][r] = s[l] == s[r] and is_palindrome[l+1][r-1]

        dp = [0] * n
        for r in range(n):
            if is_palindrome[0][r]:
                continue
            ans = inf
            for l in range(1,r+1):
                if is_palindrome[l][r]:
                    ans = min(ans,dp[l-1]+1)
            dp[r] = ans
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
