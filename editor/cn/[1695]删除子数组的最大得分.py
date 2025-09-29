# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。 
# 
#  返回 只删除一个 子数组可获得的 最大得分 。 
# 
#  如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,2,4,5,6]
# 输出：17
# 解释：最优子数组是 [2,4,5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,2,1,2,5,2,1,2,5]
# 输出：8
# 解释：最优子数组是 [5,2,1] 或 [1,2,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics 数组 哈希表 滑动窗口 👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        cur_sum = 0
        window = set()
        for r,num in enumerate(nums):
            while num in window:
                cur_sum -= nums[left]
                window.remove(nums[left])
                left += 1
            cur_sum += num
            window.add(num)
            ans = max(ans, cur_sum)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
