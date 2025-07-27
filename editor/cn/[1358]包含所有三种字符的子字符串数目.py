# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。 
# 
#  请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", 
# "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
#  
# 
#  示例 2： 
# 
#  输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
#  
# 
#  示例 3： 
# 
#  输入：s = "abc"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= s.length <= 5 x 10^4 
#  s 只包含字符 a，b 和 c 。 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right,val in enumerate(s):
            cnt[val] += 1
            while len(cnt) == 3:
                cnt[s[left]] -= 1
                if not cnt[s[left]]:
                    del cnt[s[left]]
                left += 1
            ans += left
        return ans
# leetcode submit region end(Prohibit modification and deletion)
