# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [0,1]
# 输出：2
# 说明：[0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0]
# 输出：2
# 说明：[0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [0,1,1,1,1,1,0,0,0]
# 输出：6
# 解释：[1,1,1,0,0,0] 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  
# 
#  Related Topics 数组 哈希表 前缀和 👍 794 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_cnt = {0: -1}
        ans = diff = 0
        for i,num in enumerate(nums):
            diff += 1 if num else -1
            if diff in diff_cnt:
                ans = max(ans,i-diff_cnt[diff])
            else:
                diff_cnt[diff] = i
        return ans
# leetcode submit region end(Prohibit modification and deletion)
