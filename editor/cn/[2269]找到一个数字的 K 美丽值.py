# 一个整数 num 的 k 美丽值定义为 num 中符合以下条件的 子字符串 数目： 
# 
#  
#  子字符串长度为 k 。 
#  子字符串能整除 num 。 
#  
# 
#  给你整数 num 和 k ，请你返回 num 的 k 美丽值。 
# 
#  注意： 
# 
#  
#  允许有 前缀 0 。 
#  0 不能整除任何值。 
#  
# 
#  一个 子字符串 是一个字符串里的连续一段字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num = 240, k = 2
# 输出：2
# 解释：以下是 num 里长度为 k 的子字符串：
# - "240" 中的 "24" ：24 能整除 240 。
# - "240" 中的 "40" ：40 能整除 240 。
# 所以，k 美丽值为 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：num = 430043, k = 2
# 输出：2
# 解释：以下是 num 里长度为 k 的子字符串：
# - "430043" 中的 "43" ：43 能整除 430043 。
# - "430043" 中的 "30" ：30 不能整除 430043 。
# - "430043" 中的 "00" ：0 不能整除 430043 。
# - "430043" 中的 "04" ：4 不能整除 430043 。
# - "430043" 中的 "43" ：43 能整除 430043 。
# 所以，k 美丽值为 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 10⁹ 
#  1 <= k <= num.length （将 num 视为字符串） 
#  
# 
#  Related Topics 数学 字符串 滑动窗口 👍 63 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s_num = str(num)
        ans = 0
        for i in range(len(s_num)-k+1):
            temp = int(s_num[i:i+k])
            print(temp)
            if temp and not num % temp:
                ans+=1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
