# 给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 2138 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        res = []
        for i in range(len(s)):
            c = s[:i+1]
            if c == c[::-1]:
                for i in self.partition(s[i+1:]):
                    res.append([c]+i)
        return res
# leetcode submit region end(Prohibit modification and deletion)
