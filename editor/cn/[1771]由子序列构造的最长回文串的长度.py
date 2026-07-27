# 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串： 
# 
#  
#  从 word1 中选出某个 非空 子序列 subsequence1 。 
#  从 word2 中选出某个 非空 子序列 subsequence2 。 
#  连接两个子序列 subsequence1 + subsequence2 ，得到字符串。 
#  
# 
#  返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。 
# 
#  字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。 
# 
#  回文串 是正着读和反着读结果一致的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：word1 = "cacb", word2 = "cbba"
# 输出：5
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。 
# 
#  示例 2： 
# 
#  输入：word1 = "ab", word2 = "ab"
# 输出：3
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。 
# 
#  示例 3： 
# 
#  输入：word1 = "aa", word2 = "bb"
# 输出：0
# 解释：无法按题面所述方法构造回文串，所以返回 0 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word1.length, word2.length <= 1000 
#  word1 和 word2 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 82 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        s = word1+word2
        @cache
        def dfs(i,j,l,r):
            if i >= n and not l:
                return 0
            if j<n and not r:
                return 0
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return dfs(i+1,j-1,l or i < n or j<n ,r or j>=n or i>=n)+2
            return max(dfs(i+1,j,l,r),dfs(i,j-1,l,r))
        ans = dfs(0, len(s) - 1,False,False)
        dfs.cache_clear()
        return ans
# leetcode submit region end(Prohibit modification and deletion)
