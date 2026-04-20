# 给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次： 
# 
#  
#  类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。 
#  类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。 
#  
# 
#  请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。 
# 
#  我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。 
# 
#  
#  比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "111000"
# 输出：2
# 解释：执行第一种操作两次，得到 s = "100011" 。
# 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "010"
# 输出：0
# 解释：字符串已经是交替的。
#  
# 
#  示例 3： 
# 
#  输入：s = "1110"
# 输出：1
# 解释：对第二个字符执行第二种操作，得到 s = "1010" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 要么是 '0' ，要么是 '1' 。 
#  
# 
#  Related Topics 字符串 动态规划 滑动窗口 👍 162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def switch(self,c):
        return '1' if c == '0' else '0'

    def minFlips(self, s: str) -> int:
        s = list(s)
        r = len(s)-1
        ans = 0
        for l in range(len(s)-1):
            if s[l] == s[r]:
                ans += 1
                s[l] = self.switch(s[l])
            r = l
        return ans

# leetcode submit region end(Prohibit modification and deletion)
