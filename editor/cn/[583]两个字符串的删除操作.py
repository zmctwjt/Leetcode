# 给定两个单词 word1 和
#  word2 ，返回使得
#  word1 和 
#  word2 相同所需的最小步数。 
# 
#  每步 可以删除任意一个字符串中的一个字符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
#  
# 
#  示例 2: 
# 
#  
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  1 <= word1.length, word2.length <= 500 
#  word1 和 word2 只包含小写英文字母 
#  
# 
#  Related Topics 字符串 动态规划 👍 756 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word1) + 1)
        for i,a in enumerate(word2):
            pre = 0
            for j,b in enumerate(word1):
                tmp = dp[j+1]
                if a==b:
                    dp[j+1] = pre+1
                else:
                    dp[j+1] = max(dp[j+1],dp[j])
                pre = tmp
        return len(word1)-dp[-1] + len(word2)-dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
