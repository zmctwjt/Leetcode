# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
# 
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 1111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        l = 0
        for r,c in enumerate(s2):
            while cnt[c] <= 0:
                cnt[s2[l]] += 1
                l += 1
            cnt[c] -= 1
            if r-l + 1 == len(s1):
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
